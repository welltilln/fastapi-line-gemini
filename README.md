# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight boilerplate repository for integrating Google's Gemini API with the LINE Messaging API. Built on FastAPI, this project provides a streamlined setup process, including an automated local Ngrok tunnel for rapid prototyping.

<p align="center">
    <a href="README.md"><img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English"></a>
    <a href="docs/README-TH.md"><img src="https://img.shields.io/badge/Language-%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="docs/README-ZH.md"><img src="https://img.shields.io/badge/Language-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="docs/README-JA.md"><img src="https://img.shields.io/badge/Language-%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="docs/README-KO.md"><img src="https://img.shields.io/badge/Language-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

## Architecture

```mermaid
sequenceDiagram
    participant User as LINE User
    participant LINE as LINE Platform
    participant Ngrok as Ngrok Tunnel
    participant App as FastAPI Server
    participant DB as SQLite DB
    participant Gemini as Google Gemini API

    User->>LINE: Sends Text/Image
    LINE->>Ngrok: Webhook POST Request
    Ngrok->>App: Forwards Request (Port 8000)
    App->>DB: Fetch User Chat History
    App->>Gemini: Sends Content + History + System Prompt
    Gemini-->>App: AI Response
    App->>DB: Save Updated Chat History
    App-->>LINE: Reply Message POST
    LINE-->>User: Bot Replies
```

## Features
- **Persistent Session Memory (SQLite)**: Automatically saves and restores Gemini chat histories (`chat_session`) per user in a local `sessions.db`. Server restarts will *not* wipe conversational context.
- **Zero-Configuration Launch**: Execution scripts (`run.sh` / `run.bat`) automatically manage virtual environments, dependencies, and local tunneling (Ngrok).
- **Multimodal Support**: Built-in handling for both text messages and image parsing.
- **Docker Support**: Includes a `Dockerfile` and `docker-compose.yml` for isolated production deployments.

## Prerequisites
1. Python 3.9 or higher.
2. [LINE Messaging API Credentials](https://developers.line.biz/console/): `Channel Secret` and `Channel Access Token`.
3. [Google Gemini API Key](https://aistudio.google.com/).
4. [Ngrok Auth Token](https://dashboard.ngrok.com/): Required for local development.

## Setup Instructions

### Local Development

1. Clone the repository.
2. Rename `.env.example` to `.env` and assign your API credentials.
3. Execute the startup script appropriate for your operating system:
   - **MacOS / Linux:** `./run.sh`
   - **Windows:** `run.bat`

The script will launch the FastAPI server and expose it via Ngrok. 
Copy the generated Webhook URL (e.g., `https://xxxx.ngrok.app/callback`) and configure it in your LINE Developers Console.

## Built with this Template (Examples)

Check out what you can build using this template:
- **[How Many Cals](https://github.com/welltilln/howmanycals)**: An AI-powered LINE bot that analyzes food images, extracts exact calorie counts, reads meal components, and tracks daily calorie intake using Gemini's native session memory.

### Production Deployment (Docker)

For stable, long-term hosting on a traditional VPS without Ngrok, utilize the provided Docker configuration.

1. Ensure [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/) are installed.
2. Build and run the container in detached mode:
   ```bash
   docker-compose up -d --build
   ```

## Customization

- **AI Persona**: Modify the `system_prompt` variable within `gemini.py` to adjust the model's behavior and personality.
- **Bot Logic**: Custom routing or pre-processing logic can be added to the `handle_callback()` function in `main.py`.

### Upgrading the AI Model (Future-Proofing)
If a newer, smarter Gemini model is released in the future (e.g., Gemini 3.0), you don't need to rewrite the project! Simply open `app/gemini.py` and change the `model_name` string to the new version:
```python
model = genai.GenerativeModel(
  model_name="gemini-3.0-pro", # <-- UPDATE THIS LINE
  ...
)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
