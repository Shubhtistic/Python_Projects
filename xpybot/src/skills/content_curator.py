import time
from datetime import datetime, timezone

from ..x_client import X_Client
from ..database import Json_DB
import src.config as cf



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
        query = " OR ".join(query_parts) + " -is:retweet -is:reply -is:quote lang:en has:hashtags has:links"
        max_res=cf.MAXIMUM_RESULTS_TO_SEARCH
        # max results to search for
        tweets=self._x_client.return_recent_tweets(query,max_res)

        if not tweets:
            print("No tweets found in this criteria")
            print("Exiting ..........")
            return
        rt_count=0 # retweet count
        p_count=0 # processed count
        for tweet in tweets:
            p_count += 1
            tweet_id = str(tweet.id)
            if isinstance(tweet.public_metrics, dict):
                like_count = tweet.public_metrics.get('like_count', 0)
                retweet_count = tweet.public_metrics.get('retweet_count', 0)
            else:
                like_count = 0
                retweet_count = 0

            print("--------------------------------------------------------------------------")
            print(f"Evaluating tweet {tweet_id} (Likes: {like_count}, Retweets: {retweet_count})...")

            if self._db.is_processed(tweet_id):
                print(f"  - Status: Already processed. Skipping.")
                continue

            if like_count < cf.MINIMUM_LIKE_COUNT or retweet_count < cf.MINIMUM_RETWEET_COUNT:
                print(f"  - Status: Not popular enough (Likes: {like_count} ). Skipping...")
                continue

            try:
                tweet_time = datetime.fromisoformat(tweet.created_at.replace('Z', '+00:00'))
                # tweet.created_at returns in iso format like 2025-10-24T08:15:30Z and sometimes it may fail(failed once in our code) so lets wrap in try block
                # with .replace() converts it to python equivalent utc format
                # datetime.fromisoformat conevrts it to python datetime object
                age_hours = (datetime.now(timezone.utc) - tweet_time).total_seconds() / 3600
                # datetime.now() cuurent time 
                # subtract it with tweet_time to getcuurent time of post and divide by 3600 to get in value in hours
                # 1 hour = 3600 seconds
            except Exception:
                print(f"  - Status: Could not parse created_at for tweet {tweet_id}. Skipping.")
                continue
            if age_hours < 2:
                print("Status: Too new, Skipping.")
                continue

            print("It Is new and unique, Attempting retweet")
            success = self._x_client.retweet(tweet_id)
            if success:
                self._db.add_processed_id(tweet_id)
                rt_count += 1
                print(f"Success! Retweeted and recorded tweet {tweet_id}.")
                time.sleep(3)
            else:
                print(f"Failed to retweet tweet {tweet_id}.")
                time.sleep(2)

        print(f"\n--- Content Curator Finished ---")
        print(f"Processed {p_count} tweets found.")
        print(f"Successfully retweeted {rt_count} new tweets.")