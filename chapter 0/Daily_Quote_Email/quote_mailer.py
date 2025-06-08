
import os, schedule, smtplib, requests
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

def send_quote():
    quote = requests.get("https://api.quotable.io/random").json()["content"]
    msg = EmailMessage()
    msg["Subject"] = "Your Daily Boost"
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = os.getenv("EMAIL_TO")
    msg.set_content(quote)

    with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as s:
        s.starttls(); s.login(os.getenv("EMAIL_FROM"), os.getenv("EMAIL_PASS"))
        s.send_message(msg)
        print("Sent:", quote[:60], "…")

schedule.every().day.at("07:00").do(send_quote)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
