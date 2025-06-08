
import imaplib, email, os
from dotenv import load_dotenv

load_dotenv()

box = imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"))
box.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
box.select("INBOX")

status, ids = box.search(None, '(UNSEEN SUBJECT "Run Report")')
for num in ids[0].split():
    typ, msg_data = box.fetch(num, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])
    sender = email.utils.parseaddr(msg["From"])[1]
    print("Command email from:", sender)
    # trigger your script here
box.logout()
