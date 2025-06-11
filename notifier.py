
import smtplib
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_APP_PASSWORD

def send_alert(ip, count):
    msg = EmailMessage()
    msg['Subject'] = f'[ALERT] SSH Brute Force Detected: {ip}'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content(f'Brute force attack detected from IP {ip} with {count} failed attempts.')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_APP_PASSWORD)
        smtp.send_message(msg)
