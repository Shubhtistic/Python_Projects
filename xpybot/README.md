# XpyBot - Multi-Function Twitter Bot

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Overview

XpyBot is a modular Python-based bot designed to interact with the X API (formerly Twitter API v2) using Tweepy. It performs several automated tasks: curating content based on keywords, replying to user mentions using AI (Google Gemini), and posting original content fetched from various public APIs. This project demonstrates skills in API integration, basic state management via JSON, modular design patterns (Strategy), configuration management (`.env`), and professional logging.

---

## Features (v1.0)

* **Content Curator:** Searches for recent tweets matching configured keywords (e.g., `#Python`, `#C++`, `#Rust`) and quality metrics (likes, retweets, age, verified status). Retweets qualifying content, avoiding duplicates using `.retweets.json`.
* **AI Replier:** Fetches mentions directed at the bot account (`@XPytBot`). Uses the Google Gemini API with a safety-focused system prompt to generate contextual replies. Avoids duplicate replies and self-replies using `.replies.json`.
* **Data Tracker:** Fetches random data (facts, jokes, advice) from configured public APIs (Useless Facts, Dad Jokes, Advice Slip, JokeAPI with safety filters). Posts the fetched content as an original tweet, avoiding duplicates using `.data_track.json`.
* **Modular Design:** Employs a skill-based architecture (similar to the Strategy Pattern) where each core function (Curator, Replier, Tracker) is encapsulated in its own class within the `skills` module.
* **Configuration:** Manages API keys and operational settings (like like/retweet thresholds) securely using environment variables loaded from a `.env` file via `src/config.py`.
* **Professional Logging:** Implements robust logging using Python's `logging` module. Configured via `src/log_config.py` to output `INFO` level messages (and higher) to the console and `DEBUG` level messages (and higher) to a persistent file (`xpybot.log`) for detailed diagnostics and troubleshooting. Log rotation setup is recommended for long-term deployment.

---

## Tech Stack

* **Language:** Python 3.12
* **Core Libraries:**
    * `tweepy`: For interacting with the X API v2.
    * `google-generativeai`: For interacting with the Google Gemini API.
    * `requests`: For fetching data from public APIs (used by `Data_Client`).
    * `python-dotenv`: For loading environment variables from the `.env` file.
* **Scheduling:** `cron` (recommended for Linux VPS deployment).
* **Deployment:** AWS EC2 (Ubuntu Linux recommended).

---

## Setup Instructions (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Shubhtistic/Python_Projects.git
    cd Python_Projects/xpybot
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    # On Linux/macOS
    source .venv/bin/activate
    # On Windows use:
    .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    * Copy `.env.example` to `.env`:
        ```bash
        cp .env.example .env
        ```
    * Edit the `.env` file and add your actual API keys obtained from the respective developer portals:
        * `TWITTER_API_KEY`
        * `TWITTER_API_SECRET`
        * `TWITTER_ACCESS_TOKEN`
        * `TWITTER_ACCESS_TOKEN_SECRET`
        * `TWITTER_BEARER_TOKEN`
        * `GEMINI_API_KEY`

---

## Configuration

Bot behavior can be tuned primarily in `src/config.py`:

* `KEYWORDS_TO_SEARCH`: List of hashtags/keywords for the Content Curator.
* `MINIMUM_LIKE_COUNT`, `MINIMUM_RETWEET_COUNT`: Thresholds for content curation.
* `MAXIMUM_RESULTS_TO_SEARCH`: How many tweets the Curator fetches per run.
* `MAXIMUM_MENTIONS_TO_FIND`: How many mentions the AI Replier fetches per run.

The age filter (`MIN_AGE_HOURS`, `MAX_AGE_HOURS`) for the Content Curator is currently set within `src/skills/content_curator.py`. The AI system prompt is set within `src/ai_client.py`.

---

## Usage

To run the bot manually from your project root directory (`xpybot/`):

```bash
python3 -m src.main