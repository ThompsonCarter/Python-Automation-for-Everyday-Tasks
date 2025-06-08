
from twilio.rest import Client
from dotenv import load_dotenv
import os, datetime as dt

load_dotenv()

twilio = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))

body = f"🚨 High error rate detected at {dt.datetime.now():%H:%M:%S}"
twilio.messages.create(
    to=os.getenv("TWILIO_TO"),
    from_=os.getenv("TWILIO_FROM"),
    body=body
)
print("SMS sent.")
