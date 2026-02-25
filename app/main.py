import os
import sys
import io
from dotenv import load_dotenv
load_dotenv()

from fastapi import Request, FastAPI, HTTPException
from PIL import Image

from linebot.v3.webhook import WebhookParser
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage,
    ShowLoadingAnimationRequest,
    AsyncMessagingApiBlob
)
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent, ImageMessageContent

# Make sure to implement your gemini logic in gemini.py
from app.gemini import model, extract_history_to_list
import app.database as database

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

configuration = Configuration(access_token=channel_access_token)

app = FastAPI()
async_api_client = AsyncApiClient(configuration)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(channel_secret)

@app.post("/callback")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
       
        # Restore user session from SQLite
        user_id = event.source.user_id
        history = database.get_session_history(user_id)
        chat = model.start_chat(history=history)

        # Show loading animation
        await line_bot_api.show_loading_animation(
            ShowLoadingAnimationRequest(chatId=user_id, loadingSeconds=30)
        )

        if isinstance(event.message, ImageMessageContent):
            image_binary = await AsyncMessagingApiBlob(AsyncApiClient(configuration)).get_message_content(event.message.id)
            image_buffer = io.BytesIO(image_binary)
            image = Image.open(image_buffer)
            
            # Send image to the memory-aware chat object
            response = chat.send_message(["ภาพนี้คืออะไร?", image])
            
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=response.text)]
                )
            )

        elif isinstance(event.message, TextMessageContent):
            user_text = event.message.text
            
            # Send the user text to the chat 
            response = chat.send_message(user_text)
            
            await line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=response.text)]
                )
            )

        # Save updated history to SQLite
        try:
            updated_history = extract_history_to_list(chat)
            database.save_session_history(user_id, updated_history)
        except Exception as e:
            print(f"Failed to save history: {e}")

    return 'OK'

if __name__ == "__main__":
    import uvicorn
    from pyngrok import ngrok
    import logging

    # Disable uvicorn access logs for cleaner terminal output
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    
    port = 8000
    
    # Authenticate ngrok if token is provided
    ngrok_token = os.getenv("NGROK_AUTHTOKEN")
    if ngrok_token:
        ngrok.set_auth_token(ngrok_token)
    elif not os.path.exists(os.path.expanduser("~/.ngrok2/ngrok.yml")):
        print("⚠️ Warning: NGROK_AUTHTOKEN not found. Ngrok might disconnect after a while.")
    
    # Open a ngrok tunnel to the dev server
    public_url = ngrok.connect(port).public_url
    print("\n" + "="*60)
    print("🚀 ZERO-FRICTION SERVER STARTED!")
    print(f"🔗 ngrok tunnel: {public_url} -> http://127.0.0.1:{port}")
    print(f"✅ Please update your LINE Webhook URL to: {public_url}/callback")
    print("="*60 + "\n")
    
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")
