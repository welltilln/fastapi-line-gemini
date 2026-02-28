import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

load_dotenv()

# 1. Provide your core system prompt/persona here
system_prompt = """
You are a helpful and highly intelligent AI assistant connected via a LINE bot.
Please respond concisely and informatively.
"""

generation_config = {
  "temperature": 1,
  "top_p": 0.95,    
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# 2. Configure the API Key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("Warning: GEMINI_API_KEY not found in environment variables.")

# 3. Create the model
model = genai.GenerativeModel(
  model_name="gemini-2.5-flash",
  system_instruction=system_prompt,
  generation_config=generation_config,
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
)

def extract_history_to_list(chat) -> list:
    """Extracts text-only history from a Gemini ChatSession to a local list for JSON serialization.
    Skips image blobs to save database space."""
    history = []
    for message in chat.history:
        text_parts = [part.text for part in message.parts if hasattr(part, 'text') and part.text]
        if text_parts:
            history.append({"role": message.role, "parts": text_parts})
    return history
 