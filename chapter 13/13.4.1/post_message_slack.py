
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os, json

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

try:
    response = client.chat_postMessage(
        channel=os.getenv("SLACK_CHANNEL"),
        text="🎉 Report generated! View <https://intranet/reports|here>."
    )
    print("Slack message ID:", response["ts"])
except SlackApiError as e:
    print("Error:", e.response["error"])
