# XpyBot — Multi-Function Twitter Bot

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Overview

XpyBot is a modular Python bot that interacts with the X API (formerly Twitter API v2) via Tweepy. It automates three tasks: curating and retweeting content based on keywords, replying to mentions using Google Gemini AI, and posting original content fetched from public APIs. The project demonstrates API integration, state management via JSON, modular design (Strategy pattern), configuration management with `.env`, and structured logging.

---

## Features

- **Content Curator** — Searches for recent tweets matching configured keywords (e.g. `#Python`, `#Rust`) and quality thresholds (likes, retweets, age, verified status). Retweets qualifying content; duplicate prevention via `.retweets.json`.
- **AI Replier** — Fetches mentions directed at `@XPytBot` and generates contextual replies using the Google Gemini API with a safety-focused system prompt. Duplicate and self-reply prevention via `.replies.json`.
- **Data Tracker** — Fetches content from public APIs (Useless Facts, Dad Jokes, Advice Slip, JokeAPI) and posts it as original tweets. Duplicate prevention via `.data_track.json`.
- **Modular Design** — Each core function (Curator, Replier, Tracker) is its own class within the `skills` module, following the Strategy pattern.
- **Configuration** — API keys and operational settings managed via environment variables loaded from `.env` through `src/config.py`.
- **Structured Logging** — Configured via `src/log_config.py`: `INFO`+ to console, `DEBUG`+ to `xpybot.log`. Log rotation recommended for long-term deployment.

---

## Tech Stack

- **Core:** Python 3.12, Git
- **APIs & Libraries:** Tweepy, Google Generative AI (Gemini), Requests, Boto3
- **AWS:** Lambda, S3, EventBridge, CloudWatch, IAM, SNS
- **Config & State:** `.env`, JSON

---

## Setup (Local Development)

```bash
# Clone and navigate
git clone git@github.com:Shubhtistic/Python_Projects.git
cd Python_Projects/xpybot

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and fill in your API keys
```

**Required keys in `.env`:**
- `TWITTER_API_KEY`
- `TWITTER_API_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`
- `TWITTER_BEARER_TOKEN`
- `GEMINI_API_KEY`

---

## Configuration

Tune bot behavior in `src/config.py`:

| Setting | Description |
|---|---|
| `KEYWORDS_TO_SEARCH` | Hashtags/keywords for the Content Curator |
| `MINIMUM_LIKE_COUNT` | Like threshold for curation |
| `MINIMUM_RETWEET_COUNT` | Retweet threshold for curation |
| `MAXIMUM_RESULTS_TO_SEARCH` | Tweets fetched per Curator run |
| `MAXIMUM_MENTIONS_TO_FIND` | Mentions fetched per AI Replier run |

The age filter (`MIN_AGE_HOURS`, `MAX_AGE_HOURS`) is set in `src/skills/content_curator.py`. The AI system prompt is set in `src/ai_client.py`.

---

## Usage

```bash
python3 -m src.main
```

---

## Deployment (AWS Serverless)

The bot runs as a stateless serverless application on AWS:

- **AWS Lambda** executes the core logic, triggered **4× daily** by an **Amazon EventBridge** cron schedule (`0 1,7,13,19 * * ? *`, Asia/Kolkata timezone)
- **Amazon S3** persists state files (e.g. `.replies.json`) between stateless Lambda runs
- **API keys** and resource names are managed as Lambda environment variables
- **Amazon CloudWatch** captures all logs; **Amazon SNS** sends email alerts on run success or failure
- **IAM Role** grants the Lambda function least-privilege access to S3, CloudWatch, and SNS