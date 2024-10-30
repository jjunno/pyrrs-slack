import os
from dotenv import load_dotenv
from slack_sdk import WebClient
load_dotenv()

SLACK_TOKEN=os.getenv('SLACK_TOKEN')

class Slack:
  def __init__(self):
    self.client = WebClient(token=SLACK_TOKEN)

  def send_message(self, message):
    self.client.chat_postMessage(channel='#uutiset', text=message)
