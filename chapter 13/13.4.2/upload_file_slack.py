
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

client.files_upload(
    channels=os.getenv("SLACK_CHANNEL"),
    file="reports/full_report.pdf",
    title="Full KPI Report",
    initial_comment="PDF attached."
)
