# pyrrs-slack

A single application reads single RRS feed and then sends a single message to a Slack channel containing titles and URLs for each new feed item.

Uses local store (per instance) to store up to MAX_MD5_ENTRIES entries.

You need to set up Slack and Slack app/bot for this.

# Init development

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
python3 src/main.py
```

# Run containers for productions

After setting up secret_slack_token.txt and docker-compose.yml.

```
docker compose up -d --build
```

# .env

Use .env file for development. Otherwise docker-compose.yml variables are recommended.
You might want to resolve use of secret_slack_token.txt during development.
The application expects SLACK_TOKEN_FILE env variable which contains Slack token.

```
SLACK_CHANNEL=channelname_nohashtag
RSS_FEED=https://somefeed.url.com/rss.xml
INTERVAL_MINUTES=5
MAX_MD5_ENTRIES=1000
```

# secret_slack_token.txt

Add Slack token to this secret file and use it in docker-compose.yml.

# docker-compose.yml

Example of docker-compose.yml file.

```
services:
  yle.fi:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: yle.fi
    restart: unless-stopped
    logging:
      options:
        max-size: '10m'
    environment:
      - RSS_FEED=https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss
      - INTERVAL_MINUTES=5
      - MAX_MD5_ENTRIES=1000
      - SLACK_CHANNEL=uutiset
      - SLACK_TOKEN_FILE=/run/secrets/slack_token
    secrets:
      - slack_token

secrets:
  slack_token:
    file: secret_slack_token.txt
```
