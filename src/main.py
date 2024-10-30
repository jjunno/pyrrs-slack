import os
import time
import hashlib
from dotenv import load_dotenv

import reader
import slack

load_dotenv()

RSS_FEED = os.getenv('RSS_FEED')
INTERVAL_MINUTES = int(os.getenv('INTERVAL_MINUTES'))
INTERVAL_SECONDS = INTERVAL_MINUTES * 60
MAX_MD5_ENTRIES = int(os.getenv('MAX_MD5_ENTRIES'))
SENT_MESSAGES = [] # md5 hashes of sent messages (title ::: url)

def iterator():
  r = reader.Reader(RSS_FEED)
  arr = []
  for entry in r.feed.entries:
    arr.append({entry.title: entry.link})
  return arr

def string_to_md5(title, url):
  s = f'{title} ::: {url}'
  return hashlib.md5(s.encode()).hexdigest()

def store_md5(md5):
  SENT_MESSAGES.append(md5)
  # Remove first index (oldest message) to make sure the list doesn't grow indefinitely
  if len(SENT_MESSAGES) > MAX_MD5_ENTRIES:
    SENT_MESSAGES.pop(0)

def main():
  print('Running main()')
  data = iterator()
  # 'Testiotsikko \n https://www.hs.fi \n \n Testiotsikko2 \n https://www.hs.fi'
  string = ''
  for item in data:
    for title, url in item.items():
      md5 = string_to_md5(title, url)
      if md5 in SENT_MESSAGES:
        print(f'MD5 {md5} is already sent')
        continue
      store_md5(md5)
      string += title + '\n' + url + '\n\n'
      print(f'Sending MD5 {md5}, title {title}')
  
  if string:
    slack.Slack().send_message(string)
  else:
    print('No new messages to send')
    
  
if __name__ == "__main__":
  while True:
    main()
    print(f'Sleeping for {INTERVAL_SECONDS} seconds')
    time.sleep(INTERVAL_SECONDS)
