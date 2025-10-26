import tweepy
from . import config
import sys
import logging

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

logger = logging.getLogger(__name__)

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
                # break if success
                break 
            except tweepy.TweepyException as e:
                wait_time=BACKOFF_FACTOR**attempt
                logger.warning(f"Authentication attempt {attempt} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
                ## the program pauses(sleeps) for the given time from wait_time
        else:
            ## for else block -> else only runs if the loop completed fully in our case all tries exhausted
            logger.critical("all attempts done")
            raise RuntimeError("All authentication attempts failed. Program terminating.")

    def return_recent_tweets(self,queries,max_results_limit, sort_order="relevancy",tweet_fields=["public_metrics", "created_at", "lang"]):
        try:
            responses = self.client.search_recent_tweets(query=queries,
                                                         max_results=max_results_limit,
                                                         sort_order=sort_order,
                                                         tweet_fields=tweet_fields)
            tweets=responses.data
            tweets_list=list()
            if tweets:
                for tweet in tweets:
                    tweets_list.append(tweet)
            return tweets_list
        except tweepy.TweepyException as e:
            
            logger.error(f"Error: {e}", exc_info=True)
            return [] ## empty list returned

    def retweet(self,tweet_id):
        try:
            response=self.client.retweet(tweet_id)
            
            return True
        except tweepy.TweepyException as e:
            logger.error(f"Logging Failed: {e}", exc_info=True)
            return False
        
    def get_recent_mentions(self, max_results):
        """
        Returns a list of dicts with:
        tweet_id: ID of the mention tweet
        mentioner_id: ID of the user who mentioned the bot
        mentioner_username: username of the user who mentioned the bot
        tweet_text: text content of the mention
        """
        mentions_list = list()
        try:
            mentions_response = self.client.get_users_mentions(
                id=self.client.get_me().data.id,
                max_results=max_results,
                tweet_fields=["created_at", "lang", "public_metrics", "author_id"]
            )

            mentions = mentions_response.data
            if mentions:
                for mention in mentions:
                    user_info = self.client.get_user(id=mention.author_id)
                    mentions_list.append({
                        "tweet_id": mention.id,                  
                        "mentioner_id": mention.author_id,       
                        "mentioner_username": user_info.data.username, 
                        "tweet_text": mention.text               
                    })
                    time.sleep(2)
                    # we repeatedly call it in loop so we pause a bit to avoid X rate limits
            return mentions_list

        except tweepy.TweepyException as e:
            logger.error(f"Error in fetching mentions: {e}", exc_info=True)
            return []

    def reply_to_tweet(self, reply_text, tweet_id_to_reply, mentioner_username):
        """
        parameters:
        - reply_text: the message you want to send
        - tweet_id_to_reply: ID of the tweet you are replying to
        - mentioner_username: username of the person who mentioned you
        """
        try:
            # include the mentioner so they get ntified
            final_reply = f"@{mentioner_username} {reply_text}"

            self.client.create_tweet(
                text=final_reply,
                in_reply_to_tweet_id=tweet_id_to_reply
            )

            logger.info(f"Replied successfully to tweet {tweet_id_to_reply} (mentioning @{mentioner_username})")
            return True
        except tweepy.TweepyException as e:
            logger.error(f"Failed to reply to tweet {tweet_id_to_reply}: {e}", exc_info=True)
            return False
    def post_tweet(self,text_to_post:str)->bool:
        """post an original top level text"""
        try:
            self.client.create_tweet(text=text_to_post)
            logger.info(f"Successfully posted a new tweet: {text_to_post[:50]}...")
            return True
        except tweepy.TweepyException as e:
            logger.error(f"Failed to make post: {e}", exc_info=True)
            return False

    @property
    def client(self):
        if self._client is None:
            raise RuntimeError("Twitter client is not authenticated.")
        return self._client