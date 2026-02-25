# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Google Gemini APIとLINE Messaging APIを統合するための軽量なボイラープレートリポジトリです。FastAPIをベースに構築されており、自動化されたローカルNgrokトンネルを含む、合理化されたセットアッププロセスを提供します。

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

## 主な機能
- **ゼロコンフィグ起動**: 実行スクリプト（`run.sh` / `run.bat`）が自動的に仮想環境、依存関係、Ngrokを管理します。
- **永続的セッションメモリ (SQLite)**: 各ユーザーのチャット履歴をローカルの `sessions.db` に自動的に保存・復元します。
- **マルチモーダル対応**: テキストと画像の両方を処理可能です。
- **Dockerサポート**: `Dockerfile`と`docker-compose.yml`が含まれています。

## 使い方

完全なインストール手順については、[English README](README.md)をご参照ください。
