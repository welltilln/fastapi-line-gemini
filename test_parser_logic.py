from app.bank_parser import parse_bank_message

test_cases = [
    {
        "name": "KBank Text Notification",
        "text": "กสิกรไทย: เงินเข้า 500.00บ. จาก นาย ก. ยอดเงินคงเหลือ 1,200.00บ."
    },
    {
        "name": "SCB Notification",
        "text": "SCB: ท่านได้ทำรายการโอนเงินจำนวน 150.00 บาท ไปยัง นาย ข. เมื่อวันที่ 28/02/2569 ยอดเงินคงเหลือในบัญชีคือ 850.50 บาท"
    }
]

for case in test_cases:
    print(f"Testing: {case['name']}")
    result = parse_bank_message(text=case['text'])
    print(f"Result: {result}")
    print("-" * 20)
