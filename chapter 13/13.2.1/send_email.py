
import os, smtplib, ssl
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

msg = EmailMessage()
msg["Subject"] = "Automation Bot – Daily Report Ready"
msg["From"] = os.getenv("EMAIL_USER")
msg["To"] = "team@example.com"
msg.set_content("Hi team,

Today's report is attached.

—Your Bot")

context = ssl.create_default_context()
with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
    server.starttls(context=context)
    server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
    server.send_message(msg)
print("Email sent!")
