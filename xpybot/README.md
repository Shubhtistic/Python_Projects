# XpyBot - Multi-Function Twitter Bot

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg) 
## Overview

XpyBot is a modular Python-based Twitter bot designed to interact with the X API (v2) using Tweepy. It performs several automated tasks: curating content, replying to mentions using AI, and posting original content fetched from public APIs. This project demonstrates skills in API integration, basic state management, modular design patterns (Strategy), configuration management, and professional logging.

## Features (v1.0)

* **Content Curator:** Searches for recent tweets based on configured keywords (`#Python`, `#C++`, `#Rust`) and quality metrics (likes, retweets, age, verified status), then retweets qualifying content. Avoids duplicate retweets using a JSON state file (`.retweets.json`).
* **AI Replier:** Fetches mentions directed at the bot account (`@XPytBot`). Uses the Google Gemini API to generate contextual replies based on a safety-focused system prompt. Avoids duplicate replies and self-replies using a JSON state file (`.replies.json`).
* **Data Tracker:** Fetches random interesting data (facts, jokes, advice) from various public APIs (Useless Facts, Dad Jokes, Advice Slip, JokeAPI with safety filters) and posts it as original content. Avoids duplicate posts using a JSON state file (`.data_track.json`).
* **Modular Design:** Uses a skill-based architecture (Strategy Pattern) where each core function (Curator, Replier, Tracker) is encapsulated in its own class.
* **Configuration:** Manages API keys and settings securely using a `.env` file and a central `config.py` module.
* **Professional Logging:** Implements robust logging with different levels, outputting `INFO`+ to the console and `DEBUG`+ to a file (`xpybot.log`) for detailed diagnostics. Includes log rotation setup recommendation.

## Tech Stack

* **Language:** Python 3.12
* **Core Libraries:**
    * `tweepy`: For interacting with the Twitter API v2.
    * `google-generativeai`: For interacting with the Google Gemini API.
    * `requests`: For fetching data from public APIs.
    * `python-dotenv`: For loading environment variables from `.env`.
* **Scheduling:** `cron` (when deployed on Linux VPS).
* **Deployment:** AWS EC2 (Ubuntu Linux recommended).

## Setup Instructions (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Shubhtistic/Python_Projects.git
    cd xpybot
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
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
    * Edit the `.env` file and add your actual API keys:
        * `TWITTER_API_KEY`
        * `TWITTER_API_SECRET`
        * `TWITTER_ACCESS_TOKEN`
        * `TWITTER_ACCESS_TOKEN_SECRET`
        * `TWITTER_BEARER_TOKEN`
        * `GEMINI_API_KEY`

## Configuration

Bot behavior can be tuned in `src/config.py`:

* `KEYWORDS_TO_SEARCH`: List of hashtags/keywords for the Content Curator.
* `MINIMUM_LIKE_COUNT`, `MINIMUM_RETWEET_COUNT`: Thresholds for content curation.
* `MAXIMUM_RESULTS_TO_SEARCH`: How many tweets the Curator fetches per run.
* `MAXIMUM_MENTIONS_TO_FIND`: How many mentions the AI Replier fetches per run.

The age filter (min/max hours) for the Content Curator is currently set within `src/skills/content_curator.py`.

## Usage

To run the bot manually from your project root directory (`xpybot/`):

```bash
python3 -m src.main# XpyBot - Multi-Function Twitter Bot

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg) 
## Overview

XpyBot is a modular Python-based Twitter bot designed to interact with the X API (v2) using Tweepy. It performs several automated tasks: curating content, replying to mentions using AI, and posting original content fetched from public APIs. This project demonstrates skills in API integration, basic state management, modular design patterns (Strategy), configuration management, and professional logging.

## Features (v1.0)

* **Content Curator:** Searches for recent tweets based on configured keywords (`#Python`, `#C++`, `#Rust`) and quality metrics (likes, retweets, age, verified status), then retweets qualifying content. Avoids duplicate retweets using a JSON state file (`.retweets.json`).
* **AI Replier:** Fetches mentions directed at the bot account (`@XPytBot`). Uses the Google Gemini API to generate contextual replies based on a safety-focused system prompt. Avoids duplicate replies and self-replies using a JSON state file (`.replies.json`).
* **Data Tracker:** Fetches random interesting data (facts, jokes, advice) from various public APIs (Useless Facts, Dad Jokes, Advice Slip, JokeAPI with safety filters) and posts it as original content. Avoids duplicate posts using a JSON state file (`.data_track.json`).
* **Modular Design:** Uses a skill-based architecture (Strategy Pattern) where each core function (Curator, Replier, Tracker) is encapsulated in its own class.
* **Configuration:** Manages API keys and settings securely using a `.env` file and a central `config.py` module.
* **Professional Logging:** Implements robust logging with different levels, outputting `INFO`+ to the console and `DEBUG`+ to a file (`xpybot.log`) for detailed diagnostics. Includes log rotation setup recommendation.

## Tech Stack

* **Language:** Python 3.12
* **Core Libraries:**
    * `tweepy`: For interacting with the Twitter API v2.
    * `google-generativeai`: For interacting with the Google Gemini API.
    * `requests`: For fetching data from public APIs.
    * `python-dotenv`: For loading environment variables from `.env`.
* **Scheduling:** `cron` (when deployed on Linux VPS).
* **Deployment:** AWS EC2 (Ubuntu Linux recommended).

## Setup Instructions (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Shubhtistic/Python_Projects.git
    cd xpybot
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
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
    * Edit the `.env` file and add your actual API keys:
        * `TWITTER_API_KEY`
        * `TWITTER_API_SECRET`
        * `TWITTER_ACCESS_TOKEN`
        * `TWITTER_ACCESS_TOKEN_SECRET`
        * `TWITTER_BEARER_TOKEN`
        * `GEMINI_API_KEY`

## Configuration

Bot behavior can be tuned in `src/config.py`:

* `KEYWORDS_TO_SEARCH`: List of hashtags/keywords for the Content Curator.
* `MINIMUM_LIKE_COUNT`, `MINIMUM_RETWEET_COUNT`: Thresholds for content curation.
* `MAXIMUM_RESULTS_TO_SEARCH`: How many tweets the Curator fetches per run.
* `MAXIMUM_MENTIONS_TO_FIND`: How many mentions the AI Replier fetches per run.

The age filter (min/max hours) for the Content Curator is currently set within `src/skills/content_curator.py`.

## Usage

To run the bot manually from your project root directory (`xpybot/`):

```bash
python3 -m src.main# XpyBot - Multi-Function Twitter Bot

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg) 
## Overview

XpyBot is a modular Python-based Twitter bot designed to interact with the X API (v2) using Tweepy. It performs several automated tasks: curating content, replying to mentions using AI, and posting original content fetched from public APIs. This project demonstrates skills in API integration, basic state management, modular design patterns (Strategy), configuration management, and professional logging.

## Features (v1.0)

* **Content Curator:** Searches for recent tweets based on configured keywords (`#Python`, `#C++`, `#Rust`) and quality metrics (likes, retweets, age, verified status), then retweets qualifying content. Avoids duplicate retweets using a JSON state file (`.retweets.json`).
* **AI Replier:** Fetches mentions directed at the bot account (`@XPytBot`). Uses the Google Gemini API to generate contextual replies based on a safety-focused system prompt. Avoids duplicate replies and self-replies using a JSON state file (`.replies.json`).
* **Data Tracker:** Fetches random interesting data (facts, jokes, advice) from various public APIs (Useless Facts, Dad Jokes, Advice Slip, JokeAPI with safety filters) and posts it as original content. Avoids duplicate posts using a JSON state file (`.data_track.json`).
* **Modular Design:** Uses a skill-based architecture (Strategy Pattern) where each core function (Curator, Replier, Tracker) is encapsulated in its own class.
* **Configuration:** Manages API keys and settings securely using a `.env` file and a central `config.py` module.
* **Professional Logging:** Implements robust logging with different levels, outputting `INFO`+ to the console and `DEBUG`+ to a file (`xpybot.log`) for detailed diagnostics. Includes log rotation setup recommendation.

## Tech Stack

* **Language:** Python 3.12
* **Core Libraries:**
    * `tweepy`: For interacting with the Twitter API v2.
    * `google-generativeai`: For interacting with the Google Gemini API.
    * `requests`: For fetching data from public APIs.
    * `python-dotenv`: For loading environment variables from `.env`.
* **Scheduling:** `cron` (when deployed on Linux VPS).
* **Deployment:** AWS EC2 (Ubuntu Linux recommended).

## Setup Instructions (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Shubhtistic/Python_Projects.git
    cd xpybot
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
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
    * Edit the `.env` file and add your actual API keys:
        * `TWITTER_API_KEY`
        * `TWITTER_API_SECRET`
        * `TWITTER_ACCESS_TOKEN`
        * `TWITTER_ACCESS_TOKEN_SECRET`
        * `TWITTER_BEARER_TOKEN`
        * `GEMINI_API_KEY`

## Configuration

Bot behavior can be tuned in `src/config.py`:

* `KEYWORDS_TO_SEARCH`: List of hashtags/keywords for the Content Curator.
* `MINIMUM_LIKE_COUNT`, `MINIMUM_RETWEET_COUNT`: Thresholds for content curation.
* `MAXIMUM_RESULTS_TO_SEARCH`: How many tweets the Curator fetches per run.
* `MAXIMUM_MENTIONS_TO_FIND`: How many mentions the AI Replier fetches per run.

The age filter (min/max hours) for the Content Curator is currently set within `src/skills/content_curator.py`.

## Usage

To run the bot manually from your project root directory (`xpybot/`):

```bash
python3 -m src.main