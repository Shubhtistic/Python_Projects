import sys
import time 
import random # to add a small random delay
import logging

try:
    from .database import Json_DB
    from .x_client import X_Client
    from .ai_client import AI_Client
    from .data_client import Data_Client
    from . import config
    from .log_config import logger as setup_log

    # skills
    from .skills.content_curator import Content_Curator
    from .skills.ai_reply import AI_Reply
    from .skills.data_tracker import Data_Tracker

except ImportError as e:
    print(f"CRITICAL ERROR: Failed to import modules. {e}", file=sys.stderr)
    print("Please check all files and relative imports.", file=sys.stderr)
    sys.exit(1)
except ValueError as e:
    print(f"CRITICAL ERROR: Configuration failed. {e}", file=sys.stderr)
    print("Please check your .env file.", file=sys.stderr)
    sys.exit(1)

setup_log()
# the call to the logger function of the log_config and execute all code inside it 

logger=logging.getLogger(__name__)
    # So when we did our setup_log() function earlier,
    # we set up handlers (file + console) for the global logger.
    # Now, when any other file (like eg:- main.py) calls logging.getLogger(__name__)
    # it inherits those handlers automatically.
    # we are not creating new handlers here, just using the same global configuration

def run_bot():
    logger.info("=---= Initializing XPyBot =---=")

    try:
        db_curator = Json_DB(filename=".retweets.json")
        db_replier = Json_DB(filename=".replies.json")
        db_tracker = Json_DB(filename=".data_track.json")

        x_client = X_Client()
        ai_client = AI_Client()
        data_client = Data_Client()

        curator_skill = Content_Curator(
            x_client=x_client, 
            json_db=db_curator
        )
        
        replier_skill = AI_Reply(
            x_client=x_client, 
            ai_client=ai_client, 
            db=db_replier
        )
        
        tracker_skill = Data_Tracker(
            x_client=x_client, 
            data_client=data_client, 
            db=db_tracker
        )
        logger.info("all skills initialized.")

    except Exception as e:
        logger.critical(f"CRITICAL ERROR: Failed to initialize components. {e}", exc_info=True) # <-- FIX: Removed file=sys.stderr
        sys.exit(1)

    logger.info("=---= XPyBot Initialization Complete =---=")

    try:
        logger.info("\nRunning Skill 1: Content Curator")
        # curator_skill.do_retweet()
    except Exception as e:
        logger.error(f"ERROR: Content Curator skill failed: {e}", exc_info=True) 

    time.sleep(random.randint(20, 40))

    try:
        logger.info("\nRunning Skill 2: AI Replier")
        replier_skill.perform_replies()
    except Exception as e:
        logger.error(f"ERROR: AI Replier skill failed: {e}", exc_info=True) 

    time.sleep(random.randint(20, 40))

    try:
        logger.info("\nRunning Skill 3: Data Tracker")
        tracker_skill.make_post() 
    except Exception as e:
        logger.error(f"ERROR: Data Tracker skill failed: {e}", exc_info=True) 


if __name__ == "__main__":
    run_bot()
    logger.info("\n=---= XPyBot Run Finished =---=")