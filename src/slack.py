import os
from slack_sdk import WebClient

# Read the Slack token from the Docker secret file
slack_token_file = os.getenv('SLACK_TOKEN_FILE', '/run/secrets/slack_token')
with open(slack_token_file, 'r') as file:
    SLACK_TOKEN = file.read().strip()

SLACK_CHANNEL=os.getenv('SLACK_CHANNEL')

class Slack:
  def __init__(self):
    self.client = WebClient(token=SLACK_TOKEN)
    self.channel = SLACK_CHANNEL

  def send_message(self, message):
    self.client.chat_postMessage(channel=f'#{self.channel}', text=message)
