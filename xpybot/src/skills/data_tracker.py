from ..x_client import X_Client
from ..data_client import Data_Client
from ..database import Json_DB
import sys
import logging

logger = logging.getLogger(__name__)

class Data_Tracker:
    def __init__(self,x_client:X_Client,data_client:Data_Client,db:Json_DB):
        self._x_client=x_client
        self._db=db
        self._data_client=data_client
    def make_post(self):
        try:

            data=self._data_client.get_random_data().strip()
            if not data:
                logger.warning("data was empty, cant post..")
                return
            if self._db.is_processed(data):
                logger.info("Oops like this data was processed earlier")
                logger.info("Skiping...")
                return
            logger.info("Status: New, unique content lets try to post this")
            success=self._x_client.post_tweet(text_to_post=data)
            if success:
                logger.info("Successfully posted to X.")
                self._db.add_processed_id(data)
                logger.info("Also saved to Database")
            else:
                logger.error("Failed to make a post on X, Will retry next run.")

        except Exception as e:
                    logger.critical(f"CRITICAL ERROR in Data Tracker skill: {e}", exc_info=True)
        logger.info("--- Data Tracker Skill Finished ---")