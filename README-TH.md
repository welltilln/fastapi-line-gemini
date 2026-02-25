# FastAPI-LINE-Gemini Connector

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

โปรเจค Boilerplate (ต้นแบบ) น้ำหนักเบาสำหรับการเชื่อมต่อ **Google Gemini API** เข้ากับระบบ **LINE Messaging API** พัฒนาด้วย FastAPI ช่วยให้ผู้พัฒนาสามารถนำไปต่อยอดสร้างบอท AI ได้อย่างรวดเร็ว พร้อมสคริปต์รันระบบและเปิด Ngrok Tunnel ในตัว

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

## ฟีเจอร์เด่น
- **รันได้ในคลิกเดียว (Zero-Config)**: มีสคริปต์ (`run.sh` / `run.bat`) ติดตั้ง Dependencies สร้าง Environment และขอ URL จาก Ngrok ให้ทันที
- **ความจำถาวร (SQLite)**: มีระบบฐานข้อมูล `sessions.db` คอยบันทึกประวัติการแชทของแต่ละคนเอาไว้ หมดปัญหาบอทความจำเสื่อมเมื่อเซิร์ฟเวอร์รีสตาร์ท
- **รองรับข้อความและรูปภาพ**: โมเดลสามารถคุยโต้ตอบและสแกนรูปภาพได้พร้อมๆ กัน
- **พร้อมขึ้น Production**: มี `Dockerfile` และ `docker-compose.yml` รองรับ Persistent Volume เรียบร้อย

## การติดตั้งใช้งาน

ดูรายละเอียดขั้นตอนการติดตั้งฉบับสมบูรณ์ได้ที่ [English README](README.md)
