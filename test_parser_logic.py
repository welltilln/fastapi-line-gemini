from app.bank_parser import parse_bank_message

test_cases = [
    {
        "name": "KBank Text Notification",
        "text": ":  500.00.   .  1,200.00."
    },
    {
        "name": "SCB Notification",
        "text": "SCB:  150.00    .  28/02/2569  850.50 "
    }
]

for case in test_cases:
    print(f"Testing: {case['name']}")
    result = parse_bank_message(text=case['text'])
    print(f"Result: {result}")
    print("-" * 20)
