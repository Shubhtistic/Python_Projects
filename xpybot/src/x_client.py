import tweepy
import config
print(config.TWITTER_ACCESS_TOKEN)
print(config.TWITTER_API_KEY)
print(config.TWITTER_BEARER_TOKEN)
## we are tryig to implement an backoff factor for that we need the time module
import time
# what is back-off factor it is exponential
# BACKOFF_FACTOR → a number you choose, usually ≥ 1 (common: 2).
# attempt → current retry attempt number (1 for first retry, 2 for second, etc.).
# wait_time → how long the program will pause before retrying
# example back off factor of 2
# first attemp 2 ** 1 = wait 2 seconds
# second attemp 2**2 = wait 4 seconds and so on ......
# Helps avoid hammering the API if it’s temporarily down
MAX_RETRIES=3
BACKOFF_FACTOR=1.5 # time.sleep() can easily handles floats

# also try using @Property decorator
class X_Client:
    def __init__(self):
        self._client=None
        for attempt in range(1,MAX_RETRIES+1):
            try:
                self._client = tweepy.Client(consumer_key=config.TWITTER_API_KEY,
                                             consumer_secret=config.TWITTER_API_SECRET,
                                             access_token=config.TWITTER_ACCESS_TOKEN,
                                             access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET,
                                             bearer_token=config.TWITTER_BEARER_TOKEN)
                # imp for future
                # logger object(info) -> ("Twitter client authenticated successfully.")
                break 
            except tweepy.TweepyException as e:
                wait_time=BACKOFF_FACTOR**attempt
                # in future
                # loger warining (f"Authentication attempt {attempt} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
                ## the program pauses(sleeps) for the given time from wait_time
        else:
            ## for else block -> else only runs if the loop completed fully in our case all tries exhausted
            # loger error -> print("all attempts done")
            raise RuntimeError("All authentication attempts failed. Program terminating.")

    def search_recent_tweets(self):
        try:
            queries=" OR ".join(config.KEYWORDS_TO_SEARCH)
            # The API treats the query string as a boolean search
            #"OR" is a logical operator in Twitter search queries
            responses=self.client.search_recent_tweets(query=queries,max_results=10,tweet_fields=["public_metrics"])
            tweets=responses.data
            tweets_list=list()
            if tweets:
                for tweet in tweets:
                    tweets_list.append(tweet)
            return tweets_list
        except tweepy.TweepyException as e:
            # loggig log error problem in search recent {e}
            print(f"Error: {e}")
            return [] ## empty list returned  fail

    def retweet(self,tweet_id):
        try:
            response=self.client.retweet(tweet_id)
            
            return True
        except tweepy.TweepyException as e:
            # logging object -> error print(e)
            print(f"Logging Failed: {e}")
            return False

    @property
    def client(self):
        if self._client is None:
            raise RuntimeError("Twitter client is not authenticated.")
        return self._client
