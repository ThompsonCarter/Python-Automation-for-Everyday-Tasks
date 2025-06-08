# Code for connecting to email and searching for message
import os
import imap_tools
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("EMAIL_USER")
PASS = os.getenv("EMAIL_PASS")
SERVER = os.getenv("IMAP_SERVER")

with imap_tools.MailBox(SERVER).login(USER, PASS) as mailbox:
    messages = mailbox.fetch('(SUBJECT "Weekly Sales")', limit=1)
    msg = next(iter(messages), None)