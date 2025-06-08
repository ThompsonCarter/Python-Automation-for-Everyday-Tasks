
from twilio.rest import Client
from slack_sdk import WebClient
import os

class Notifier:
    def __init__(self):
        from dotenv import load_dotenv; load_dotenv()
        self.twilio = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
        self.slack = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

    def email(self, subject, body, attachments=[]):
        # … (reuse 13.2.1 code)
        pass

    def sms(self, body):
        self.twilio.messages.create(
            to=os.getenv("TWILIO_TO"),
            from_=os.getenv("TWILIO_FROM"),
            body=body)

    def slack_msg(self, text):
        self.slack.chat_postMessage(channel=os.getenv("SLACK_CHANNEL"), text=text)
