# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Google의 Gemini API를 LINE Messaging API와 통합하기 위한 경량 보일러플레이트 저장소입니다. FastAPI를 기반으로 구축되었으며 자동화된 로컬 Ngrok 터널을 포함하여 간소화된 설정 프로세스를 제공합니다.

<p align="center">
    <a href="README.md">English</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-TH.md">ภาษาไทย</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-ZH.md">简体中文</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-JA.md">日本語</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-KO.md">한국어</a>
</p>

## 주요 기능
- **구성 없는 시작**: 실행 스크립트(`run.sh` / `run.bat`)는 가상 환경, 종속성 및 Ngrok 터널링을 자동으로 관리합니다.
- **영구 세션 메모리(SQLite)**: 로컬 `sessions.db`에 채팅 기록을 자동으로 저장하고 복원합니다.
- **멀티모달 지원**: 텍스트 메시지 및 이미지 분석 모두 지원합니다.
- **Docker 지원**: 격리된 배포 환경을 위한 `Dockerfile` 및 `docker-compose.yml`이 포함되어 있습니다.

## 시작하기

자세한 설정 방법은 [English README](README.md)를 참조하십시오.
