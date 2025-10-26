import time
from datetime import datetime, timezone

from ..x_client import X_Client
from ..database import Json_DB
from .. import config as cf
import logging

logger = logging.getLogger(__name__)


#Dependency Injection in simple terms
#Instead of the class creating its own dependencies, you “inject” them from outside.
#Your class only uses the objects; it doesn’t care how they were created
class Content_Curator:
    def __init__(self,x_client:X_Client,json_db:Json_DB):
        #store instances as private members
        self._x_client=x_client
        self._db=json_db


    def do_retweet(self):
        query_parts = [f"({keyword})" for keyword in cf.KEYWORDS_TO_SEARCH]
        # list comprehension
        # each keyword will be wrapped in ()
        query = " OR ".join(query_parts) + " -is:retweet -is:reply -is:quote lang:en has:hashtags has:links is:verified"
        max_res=cf.MAXIMUM_RESULTS_TO_SEARCH
        # max results to search for
        tweets=self._x_client.return_recent_tweets(query,max_res)

        if not tweets:
            logger.info("No tweets found in this criteria")
            logger.info("Exiting ..........")
            return
        rt_count=0 # retweet count
        p_count=0 # processed count
        for tweet in tweets:
            p_count += 1
            tweet_id = str(tweet.id)
            if tweet.public_metrics is not None:
                like_count = tweet.public_metrics.get('like_count', 0)
                retweet_count = tweet.public_metrics.get('retweet_count', 0)
            else:
                like_count = 0
                retweet_count = 0

            logger.info("--------------------------------------------------------------------------")
            logger.info(f"Evaluating tweet {tweet_id} (Likes: {like_count}, Retweets: {retweet_count})...")

            if self._db.is_processed(tweet_id):
                logger.info(f"Status :- Already processed, Skipping....")
                continue

            if like_count < cf.MINIMUM_LIKE_COUNT or retweet_count < cf.MINIMUM_RETWEET_COUNT:
                logger.info(f"Status: Not popular enough (Likes: {like_count} ), Skipping...")
                continue

            try:
                if not tweet.created_at:
                    logger.warning(f"Status: Tweet {tweet_id} missing created_at field, Skipping....")
                    continue

                MIN_AGE_HOURS = 0.25  # 15 minutes
                MAX_AGE_HOURS = 12    # 12 hours
                tweet_time = tweet.created_at
            
                age_hours = (datetime.now(timezone.utc) - tweet_time).total_seconds() / 3600
                # datetime.now() cuurent time 
                # subtract it with tweet_time to get cuurent time of post and divide by 3600 to get in value in hours
                # 1 hour = 3600 seconds

                if age_hours < MIN_AGE_HOURS:
                    logger.info(f"Status: Too new ({age_hours:.2f}h). Waiting for it to mature. Skipping..")
                    continue
                
                if age_hours > MAX_AGE_HOURS:
                    logger.info(f"Status: Too old ({age_hours:.2f}h). Skipping.")
                    continue
            except Exception as e:
                logger.warning(f"Status: Error processing age for tweet {tweet_id}, Error: {e} Skipping..", exc_info=True)
                continue


            logger.info("It Is new and unique, Attempting retweet")
            success = self._x_client.retweet(tweet_id)
            if success:
                self._db.add_processed_id(tweet_id)
                rt_count += 1
                logger.info(f"Success! Retweeted and recorded tweet {tweet_id}.")
                time.sleep(3)
            else:
                logger.error(f"Failed to retweet tweet {tweet_id}.")
                time.sleep(2)

        logger.info(f"\n--- Content Curator Finished ---")
        logger.info(f"Processed {p_count} tweets found.")
        logger.info(f"Successfully retweeted {rt_count} new tweets.")