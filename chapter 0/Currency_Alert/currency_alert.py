
import os, requests, pandas as pd
from twilio.rest import Client
from dotenv import load_dotenv; load_dotenv()

THRESHOLD = 1500     # change to suit
url = "https://open.er-api.com/v6/latest/USD"
rate = requests.get(url).json()["rates"]["NGN"]

if rate > THRESHOLD:
    body = f"⚠️ USD/NGN is {rate}"
    twilio = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
    twilio.messages.create(from_=os.getenv("TWILIO_FROM"),
                           to=os.getenv("TWILIO_TO"),
                           body=body)
    print("Alert sent.")
else:
    print("All calm.")
