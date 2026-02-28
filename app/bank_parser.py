import os
from typing import Optional, Dict
from google import genai
from google.genai import types

# Setup client (Using the modern google-genai SDK)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model_id = "gemini-1.5-flash"

BANK_PARSER_PROMPT = """
You are a banking transaction parser for Thai banks (KBank, SCB).
Extract the following information from the text or image provided:
1. bank: (scb, kbank)
2. type: (income, expense, adjustment)
3. amount: (float)
4. balance: (float, if present)
5. description: (short summary)

Return the result in JSON format ONLY. 
If the message is not a bank transaction, return {"error": "not_bank_msg"}.

Example Text: "กสิกรไทย: เงินเข้า 500.00บ. จาก นาย ก. ยอดเงินคงเหลือ 1,200.00บ."
Output: {"bank": "kbank", "type": "income", "amount": 500.0, "balance": 1200.0, "description": "เงินเข้าจาก นาย ก."}
"""

def parse_bank_message(text: str = None, image: bytes = None) -> Optional[Dict]:
    content = [BANK_PARSER_PROMPT]
    if text:
        content.append(f"Text to parse: {text}")
    if image:
        import io
        from PIL import Image
        img = Image.open(io.BytesIO(image))
        content.append(img)
    
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=content,
            config=types.GenerateContentConfig(
                response_mime_type='application/json'
            )
        )
        
        import json
        # The modern SDK handles JSON extraction better with mime_type
        return json.loads(response.text)
    except Exception as e:
        print(f"Parsing error: {e}")
        return None
