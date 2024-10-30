import os
import time

from dotenv import load_dotenv

import reader
import slack

load_dotenv()

RSS_FEED = os.getenv('RSS_FEED')
INTERVAL_MINUTES = int(os.getenv('INTERVAL_MINUTES'))
INTERVAL_SECONDS = INTERVAL_MINUTES * 60

def iterator():
  r = reader.Reader(RSS_FEED)
  arr = []
  for entry in r.feed.entries:
    # slack.Slack().send_message(entry.link)
    arr.append({entry.title: entry.link})
  # print(arr)
  return arr

def main():
  data = iterator()
  # 'Testiotsikko \n https://www.hs.fi \n \n Testiotsikko2 \n https://www.hs.fi'
  string = ''
  for item in data:
    for key, value in item.items():
      string += key + '\n' + value + '\n\n'
  
  if string:
    slack.Slack().send_message(string)
  
if __name__ == "__main__":
  while True:
    main()
    time.sleep(INTERVAL_SECONDS)
