# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

 **Google  Gemini AI**  **LINE Messaging API**  FastAPI  Ngrok 

<p align="center">
    <a href="../README.md"><img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English"></a>
    <a href="README-TH.md"><img src="https://img.shields.io/badge/Language-%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="README-ZH.md"><img src="https://img.shields.io/badge/Language-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="README-JA.md"><img src="https://img.shields.io/badge/Language-%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="README-KO.md"><img src="https://img.shields.io/badge/Language-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

---

##  (Architecture)

```mermaid
sequenceDiagram
    participant User as LINE 
    participant LINE as LINE 
    participant Ngrok as Ngrok 
    participant App as FastAPI 
    participant DB as SQLite 
    participant Gemini as Google Gemini API

    User->>LINE: 
    LINE->>Ngrok:  Webhook POST 
    Ngrok->>App:  8000 
    App->>DB: 
    App->>Gemini:  ( +  + ) 
    Gemini-->>App:  AI 
    App->>DB: 
    App-->>LINE: Reply Message 
    LINE-->>User: 
```

---

##  (Features)
- ** (SQLite):** `chat_session`  `sessions.db`  AI 
- ** (Zero-Config Launch):** Mac/Linux  `run.sh`Windows  `run.bat` Ngrok 
- ** (Multimodal):**  Blob  Gemini Vision 
- ** (Docker Ready):**  `Dockerfile`  `sessions.db`  `docker-compose.yml`

---

##  (Setup Instructions)

### 
1.  Python 3.9 
2. **[LINE Messaging API](https://developers.line.biz/console/):**  `Channel Secret`  `Channel Access Token` 
3. **[Google Gemini API Key](https://aistudio.google.com/):**  Key
4. **[Ngrok ](https://dashboard.ngrok.com/):** ()

### 

1. :
   ```bash
   git clone https://github.com/welltilln/fastapi-line-gemini.git
   cd fastapi-line-gemini
   ```
2.  `.env.example`  `.env` API Keys 
3. :
   - **MacOS  Linux :** `./run.sh`
   - **Windows :** `run.bat`
4. Ngrok  `https://xxxx.ngrok.app/callback` Line Developer  Webhook URL 

###  (Docker)
 VPS :
```bash
docker-compose up -d --build
```
`sessions.db` 

---

## 

- **[How Many Cals ()](https://github.com/welltilln/howmanycals)**:  LINE 

---

##  (Customization)

- ** AI  (Language & Persona):**
 **** `app/gemini.py`  `system_prompt`

****
```python
system_prompt = """
 AI 
 100% 

"""
```

****
```python
system_prompt = """




"""
```

###  (Future-Proofing)
 Gemini 3.0 `app/gemini.py` `model_name` 
```python
model = genai.GenerativeModel(
  model_name="gemini-3.0-pro", # <-- 
  ...
)
```

---

##  (FAQ)

**Q:  LINE **
A:  Ngrok  2  Webhook  `run.sh` 

**Q: Docker **
A:  `requirements.txt` `docker-compose up -d --build` 

## 
 MIT License  [LICENSE](../LICENSE) 
