# this module i.e config.py, the main responsibilty is too load our critical info like api keys and othe info from .env file
# by doing this we can just import config.py and just use this config file in every file we need the credentials

import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# our defined keywords to search for
KEYWORDS_TO_SEARCH = ["#Python", "#C++","#Rust"]
MINIMUM_LIKE_COUNT = 30
MINIMUM_RETWEET_COUNT=5
MAXIMUM_RESULTS_TO_SEARCH=10


MIN_AGE_HOURS = 0.25  # 15 minutes
MAX_AGE_HOURS = 48   # 48 hours



MAXIMUM_MENTIONS_TO_FIND=10
# to see if all info is loaded properly
if not all([TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET]):
    raise ValueError("Missing one or more required Twitter API v1.0a credentials in .env file")

## the program will not start is there is any error with credentials 
## raise value error

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")