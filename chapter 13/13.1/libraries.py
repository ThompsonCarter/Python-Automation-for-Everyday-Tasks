
import os
from dotenv import load_dotenv
load_dotenv()

# Libraries for various integrations
# Sending email
import smtplib
# Reading email
import imaplib
import email
# SMS & WhatsApp
from twilio.rest import Client
# Slack / Teams
from slack_sdk import WebClient
