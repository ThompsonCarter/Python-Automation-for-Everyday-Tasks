# Code for sending email
import smtplib
from email.message import EmailMessage

msg_out = EmailMessage()
msg_out["Subject"] = f"Weekly Sales Report {pd.Timestamp.today():%Y-%m-%d}"
msg_out["From"] = USER
msg_out["To"] = USER  # or team list
msg_out.set_content("Please find attached the weekly sales report.")

with open(report, "rb") as f:
    msg_out.add_attachment(f.read(), maintype="application",
                           subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                           filename=report.name)

with smtplib.SMTP("smtp.example.com", 587) as smtp:
    smtp.starttls()
    smtp.login(USER, PASS)
    smtp.send_message(msg_out)
    print("Email sent.")