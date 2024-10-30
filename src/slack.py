import os
from dotenv import load_dotenv
from slack_sdk import WebClient
load_dotenv()

SLACK_TOKEN=os.getenv('SLACK_TOKEN')
SLACK_CHANNEL=os.getenv('SLACK_CHANNEL')

class Slack:
  def __init__(self):
    self.client = WebClient(token=SLACK_TOKEN)
    self.channel = SLACK_CHANNEL

  def send_message(self, message):
    self.client.chat_postMessage(channel=f'#{self.channel}', text=message)
