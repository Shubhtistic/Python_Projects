from ..x_client import X_Client
from ..ai_client import AI_Client
from ..database import Json_DB
from .. import config as cf
import logging

logger = logging.getLogger(__name__)

class AI_Reply:
    def __init__(self,x_client:X_Client,ai_client:AI_Client,db:Json_DB):
        self._x_client=x_client
        self._ai_client=ai_client
        self._db=db
    def perform_replies(self):
        mentions_list=self._x_client.get_recent_mentions(cf.MAXIMUM_MENTIONS_TO_FIND)
        if not mentions_list:
            logger.info("No mentions found, Exiting .....")
            return
        for mention in mentions_list:
            mention_tweet_id = mention["tweet_id"]
            if(self._db.is_processed(mention_tweet_id)):
                continue
            mentioner_username = mention["mentioner_username"]
            mention_text = mention["tweet_text"]

            logger.info(f"replying to {mentioner_username} using AI ...")

            ai_reply_text = self._ai_client.ai_reply(mention_text)

            if not ai_reply_text:
                logger.warning(f"AI failed to generate reply for tweet {mention_tweet_id}")
                continue
            
            reply_status=self._x_client.reply_to_tweet(reply_text=ai_reply_text,
                                                       tweet_id_to_reply=mention_tweet_id,
                                                       mentioner_username=mentioner_username)

    
            if reply_status:
                logger.info(f"successfully replied to @{mentioner_username}")
                # Optionally store the replied tweet ID to avoid duplicate replies
                self._db.add_processed_id(mention_tweet_id)
            else:
                logger.error(f"failed to reply to @{mentioner_username}")