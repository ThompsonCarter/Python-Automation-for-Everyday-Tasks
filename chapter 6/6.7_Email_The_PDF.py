# Step 5: Email the PDF
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email_with_report():
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    SMTP_SERVER = os.getenv("SMTP_SERVER")

    pdf_file = "output/final_report_2025-05.pdf"

    msg = EmailMessage()
    msg["Subject"] = "Monthly Sales Report – May 2025"
    msg["From"] = EMAIL_USER
    msg["To"] = "team@example.com"
    msg.set_content("Hi team, please find attached the sales report for May 2025.")

    with open(pdf_file, "rb") as f:
        data = f.read()
    msg.add_attachment(data, maintype="application", subtype="pdf", filename="final_report_2025-05.pdf")

    with smtplib.SMTP(SMTP_SERVER, 587) as s:
        s.starttls()
        s.login(EMAIL_USER, EMAIL_PASS)
        s.send_message(msg)
        print("Email sent with report.")
