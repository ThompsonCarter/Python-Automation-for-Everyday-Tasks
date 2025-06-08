
from flask import Flask, request, make_response
import subprocess, json, os

app = Flask(__name__)
SLACK_SIGNING = os.getenv("SLACK_SIGNING_SECRET")

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.get_json()
    if "challenge" in data:              # URL verification
        return make_response(data["challenge"], 200)
    text = data["event"].get("text", "")
    if "run report" in text.lower():
        subprocess.Popen(["python", "generate_report.py"])
    return "", 200
