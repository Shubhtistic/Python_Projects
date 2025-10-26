import logging
import sys

def logger():
    log=logging.getLogger()
    # a root global logger object -> logging.getLogger() with no name
    # whenever we do log.info() , long.error() 
    # this single object will send your message to all active handlers
    # handlers decide where our logs go
    # you can attach multiple handlers to one logger

    log.setLevel(logging.DEBUG)
    # by set level we mean catch any message that is higher than Debug
    # Levels =>  DEBUG < INFO < WARNING < ERROR < CRITICAL
    # now the logger can take messages we need to tell it where to store or display them


    if log.hasHandlers():
        log.handlers.clear()
    #Explanation:-
    # When we call logg.getLogger() Python gives us the same global logger object for that process
    # If we call it 10 times during runtime, it’s the same object (same handlers, same configuration).
    # That’s why we have to clear() handlers — otherwise they pile up within that running process.
    #Each message we log (like log.info("Hello")) will then be printed multiple times — one copy per handler
    #log.hasHandlers() -> checks if this logger already has handlers attached.
    #log.handlers.clear() -> removes all the old ones (reset)

    try:
        log_file=logging.FileHandler("xpybot.log",mode="a",encoding='utf-8')
        # filehandler tells the logger to  write all messages to the log file xpybot.log

        log_file.setLevel(logging.DEBUG)
        # all messaggges debug and above will go in this file
        # Why use DEBUG now?
        # because DEBUG is noisy, tweepy logs are big error traceback is big
        # this is normal for DEBUG level, it shows everything.
        # our INFO message (from our code) is still one line.
        # DEBUG just saves more stuff from libraries.
        # What happens if use INFO instead
        # if we change log_config.py file_handler.setLevel(logging.INFO)
        # then xpybot.log file ONLY get INFO, WARNING, ERROR, CRITICAL.
        # NO DEBUG messages saved.
        # log file looks clean mostly one line
        # BUT
        # we lose all the DEBUG details from tweepy.
        # cannot see traceback for errors maybe.

        file_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # our decided time format

        log_file.setFormatter(file_format)

        log.addHandler(log_file)
        #Now every message sent to log.info() log.debug() etc will also be written to xpybot.log.
    except Exception as e:
        print("Failed to open log file",file=sys.stderr)
    try:
        # sys.stdout is the stream for our console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO) 
        
        console_formatter = logging.Formatter(
            '%(levelname)s - %(name)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        
        log.addHandler(console_handler)
    except Exception as e:
        print(f"CRITICAL: Failed to set up console logger: {e}", file=sys.stderr)
    log.info("Logging started")