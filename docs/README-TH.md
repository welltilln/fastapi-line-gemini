# FastAPI-LINE-Gemini Connector

<p align="center">
    <a href="../README.md"><img src="https://img.shields.io/badge/Language-English-blue?style=for-the-badge" alt="English"></a>
    <a href="README-TH.md"><img src="https://img.shields.io/badge/Language-%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2-green?style=for-the-badge" alt="Thai"></a>
    <a href="README-ZH.md"><img src="https://img.shields.io/badge/Language-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-yellow?style=for-the-badge" alt="Chinese"></a>
    <a href="README-JA.md"><img src="https://img.shields.io/badge/Language-%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=for-the-badge" alt="Japanese"></a>
    <a href="README-KO.md"><img src="https://img.shields.io/badge/Language-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey?style=for-the-badge" alt="Korean"></a>
</p>

---

## ภาพรวม (Overview)
เครื่องมือสำหรับเชื่อมต่อ **Google Gemini API** เข้ากับ **LINE Messaging API** โดยใช้ FastAPI พร้อมระบบ Ngrok Tunnel อัตโนมัติสำหรับการพัฒนาในเครื่อง

## ฟีเจอร์หลัก (Features)
- **หน่วยความจำ SQLite:** บันทึกประวัติการแชทรายบุคคล
- **ระบบรันอัตโนมัติ:** สคริปต์รันครั้งเดียวจบ (`run.sh` / `run.bat`)
- **รองรับ Multimodal:** ส่งได้ทั้งข้อความและรูปภาพ
- **รองรับ Docker:** มาพร้อม Dockerfile สำหรับใช้งานบนเซิร์ฟเวอร์จริง

## การเริ่มใช้งาน
1. ติดตั้ง Python และรับ API Key จาก LINE และ Google
2. ตั้งค่าไฟล์ `.env`
3. รันสคริปต์ `./run.sh`

## ลิขสิทธิ์
MIT License
