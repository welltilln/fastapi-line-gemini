# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Google Gemini API  LINE Messaging API FastAPI NgrokSQLite

<p align="center">
    <a href="../README.md">English</a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-TH.md"></a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-ZH.md"></a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-JA.md"></a>
    <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
    <a href="README-KO.md"></a>
</p>

---

##  (Architecture)

```mermaid
sequenceDiagram
    participant User as LINE 
    participant LINE as LINE 
    participant Ngrok as Ngrok 
    participant App as FastAPI 
    participant DB as SQLite DB
    participant Gemini as Google Gemini API

    User->>LINE: 
    LINE->>Ngrok: Webhook POST 
    Ngrok->>App:  ( 8000)
    App->>DB: 
    App->>Gemini:  +  + 
    Gemini-->>App: AI
    App->>DB: SQLite
    App-->>LINE: Reply API 
    LINE-->>User: 
```

---

##  (Features)
- ** (Persistent Memory):** RAM `sessions.db`SQLite
- **:** Mac/Linux `run.sh`  Windows `run.bat`Ngrok
- **:** GeminiAPI
- **Docker :** `Dockerfile`  `docker-compose.yml` 

---

##  (Setup Instructions)

### 
1. Python  3.9 
2. **[LINE Messaging API](https://developers.line.biz/console/):**  `Channel Secret`  `Channel Access Token` 
3. **[Google Gemini API Key](https://aistudio.google.com/):** API
4. **[Ngrok Auth Token](https://dashboard.ngrok.com/):** 

### 

1. :
   ```bash
   git clone https://github.com/welltilln/fastapi-line-gemini.git
   cd fastapi-line-gemini
   ```
2. `.env.example`  `.env` API
3. :
   - **MacOS / Linux:** `./run.sh`
   - **Windows:** `run.bat`
4.  Ngrok URL: `https://xxxx.ngrok.app/callback`LINE Developers Console  **Webhook URL** 

###  (Docker)
VPS:
```bash
docker-compose up -d --build
```
**

---

## 

- **[How Many Cals (AI )](https://github.com/welltilln/howmanycals)**: 

---

##  (Customization)

- **AI (Language & Persona):**
 **** `app/gemini.py`  `system_prompt` 

****
```python
system_prompt = """
AI


"""
```

**AI:**
```python
system_prompt = """
AI

"""
```

### AI  (Future-Proofing)
 Gemini Gemini 3.0 `app/gemini.py` `model_name` 
```python
model = genai.GenerativeModel(
  model_name="gemini-3.0-pro", # <-- 
  ...
)
```

---

##  (FAQ)

**Q: 2LINE**
A:  Ngrok 2 `run.sh` URLVPSDocker

**Q: **
A: LINEMBGemini

## 
 MIT [LICENSE](../LICENSE) 
