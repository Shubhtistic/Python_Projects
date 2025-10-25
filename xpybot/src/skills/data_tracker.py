from ..x_client import X_Client
from ..data_client import Data_Client
from ..database import Json_DB
import sys

class Data_Tracker:
    def __init__(self,x_client:X_Client,data_client:Data_Client,db:Json_DB):
        self._x_client=x_client
        self._db=db
        self._data_client=data_client
    def make_post(self):
        try:

            data=self._data_client.get_random_data().strip()
            if not data:
                print("data was empty, cant post..")
                return
            if self._db.is_processed(data):
                print("Oops like this data was processed earlier")
                print("Skiping...")
                return
            print("Status: New, unique content lets try to post this")
            success=self._x_client.post_tweet(text_to_post=data)
            if success:
                print("Successfully posted to X.")
                self._db.add_processed_id(data)
                print("Also saved to Database")
            else:
                print("Failed to make a post on X, Will retry next run.", file=sys.stderr)

        except Exception as e:
                    print(f"CRITICAL ERROR in Data Tracker skill: {e}", file=sys.stderr)
        print("--- Data Tracker Skill Finished ---")
        