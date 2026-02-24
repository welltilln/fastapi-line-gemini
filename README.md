# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight boilerplate repository for integrating Google's Gemini API with the LINE Messaging API. Built on FastAPI, this project provides a streamlined setup process, including an automated local Ngrok tunnel for rapid prototyping.

## Architecture

```mermaid
sequenceDiagram
    participant User as LINE User
    participant LINE as LINE Platform
    participant Ngrok as Ngrok Tunnel
    participant App as FastAPI Server
    participant Gemini as Google Gemini API

    User->>LINE: Sends Text/Image
    LINE->>Ngrok: Webhook POST Request
    Ngrok->>App: Forwards Request (Port 8000)
    App->>Gemini: Sends Content + System Prompt
    Gemini-->>App: AI Response
    App-->>LINE: Reply Message POST
    LINE-->>User: Bot Replies
```

## Features
- **Zero-Configuration Launch**: Execution scripts (`run.sh` / `run.bat`) automatically manage virtual environments, dependencies, and local tunneling (Ngrok).
- **Session Memory**: Utilizes Gemini's chat sessions (`chat_session`) to maintain conversation context.
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
- 🥘 **[How Many Cals](https://github.com/welltilln/howmanycals)**: An AI-powered LINE bot that analyzes food images, extracts exact calorie counts, reads meal components, and tracks daily calorie intake using Gemini's native session memory.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
