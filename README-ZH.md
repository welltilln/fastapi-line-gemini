# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个轻量级的模板仓库，用于将 Google 的 Gemini API 与 LINE Messaging API 集成。基于 FastAPI 构建，本项目提供简化的设置流程，并自带自动化的本地 Ngrok 隧道，以实现快速原型设计。

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

## 主要特性
- **零配置启动**: 执行脚本（`run.sh` / `run.bat`）自动管理虚拟环境、依赖项和本地内网穿透（Ngrok）。
- **持久化会话记忆 (SQLite)**: 在本地 `sessions.db` 中自动保存和恢复用户的聊天记录。服务器重启不会丢失对话上下文。
- **多模态支持**: 内置对文本消息和图像解析的处理。
- **Docker 支持**: 包含 `Dockerfile` 和 `docker-compose.yml`，适用于隔离的生产环境部署。

## 快速指南

有关完整的安装步骤和更多配置，请参阅 [English README](README.md)。
