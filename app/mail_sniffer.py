import imaplib
import email
from email.header import decode_header
import time
import asyncio
import os
from app.bank_parser import parse_bank_message
import sys

# Insert Yosafe path
sys.path.append("/Users/welltilln/Projects/Yosafe")
import database as yosafe_db

async def monitor_email():
    """
    Background worker that checks for new bank emails every 60 seconds.
    """
    mail_user = os.getenv("EMAIL_USER")
    mail_pass = os.getenv("EMAIL_PASS")
    mail_server = os.getenv("EMAIL_IMAP_SERVER", "imap.gmail.com")

    if not mail_user or not mail_pass:
        print("Mail Sniffer: EMAIL_USER or EMAIL_PASS not set. Skipping...")
        return

    print(f"Silent Mail Sniffer started for {mail_user}...")

    while True:
        try:
            # Login to IMAP
            mail = imaplib.IMAP4_SSL(mail_server)
            mail.login(mail_user, mail_pass)
            
            # Try to select 'BankNotif' label first, fallback to 'inbox'
            status, _ = mail.select("BankNotif")
            if status != "OK":
                mail.select("inbox")

            status, messages = mail.search(None, 'UNSEEN')
            
            if status == "OK":
                email_ids = messages[0].split()
                if email_ids:
                    print(f"Found {len(email_ids)} new emails to process...")
                
                for num in email_ids:
                    status, data = mail.fetch(num, "(RFC822)")
                    if status != "OK":
                        continue

                    raw_email = data[0][1]
                    msg = email.message_from_bytes(raw_email)
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    print(f"Processing: {subject}")
                    
                    # Extract body
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/plain" or content_type == "text/html":
                                part_body = part.get_payload(decode=True).decode()
                                body += part_body
                    else:
                        body = msg.get_payload(decode=True).decode()

                    # Parse with Gemini
                    bank_info = parse_bank_message(text=body)
                    
                    if bank_info and "error" not in bank_info:
                        try:
                            # Update Yosafe
                            account, _ = yosafe_db.Account.get_or_create(
                                name=bank_info['bank'].upper(), 
                                defaults={'type': 'Bank'}
                            )
                            yosafe_db.Transaction.create(
                                account=account,
                                amount=bank_info['amount'],
                                description=bank_info['description'],
                                type=bank_info['type']
                            )
                            if 'balance' in bank_info:
                                account.balance = bank_info['balance']
                                account.save()
                            
                            print(f"Auto-synced {bank_info['bank'].upper()}: {bank_info['amount']} THB")
                            
                        except Exception as e:
                            print(f"Error updating DB from email: {e}")

            mail.logout()
        except Exception as e:
            print(f"Mail Sniffer error: {e}")
        
        await asyncio.sleep(60)
