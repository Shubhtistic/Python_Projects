import requests
import random  
import sys    
import logging

logger = logging.getLogger(__name__)

class Data_Client:

    _FACT_API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"
    _DAD_JOKE_API_URL = "https://icanhazdadjoke.com/"
    _ADVICE_API_URL = "https://api.adviceslip.com/advice"
    

    _JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?type=single&blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    def __init__(self):
        """Has 4 Apis:
        1)useless fact api 2)Dad jokes api 3)Advice slip api 4) General jokes api\n
        Use get_random_data() method to randomly call any api"""
        logger.info(" Data Client Initilized with 4 apis")

    def _get_useless_fact(self) -> str | None:
        """fetch a useless fact from the useless facts Api\n
        Note: this is an Private function"""
        logger.info("trying to fetch a useless fact...")
        try:
            response = requests.get(self._FACT_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            fact = data.get('text')
            if not fact:
                logger.warning("'text' field missing in response")
                return None
            return f"Here's a useless fact:\n{fact}"
        except Exception as e:
            logger.error(f"Api error: {e}", exc_info=True)
            return None

    def _get_dad_joke(self) -> str | None:
        """fetches a joke from the dad jokes Api"""
        logger.info("Attempting to fetch a dad joke...")
        try:
            # this api requires an header to get an json response
            headers = {'Accept': 'application/json'}
            response = requests.get(self._DAD_JOKE_API_URL, headers=headers, timeout=10)
            response.raise_for_status()
            # any https error
            data = response.json()
            # json format -> {"joke": "..."}
            dad_joke = data.get('joke')
            if not dad_joke:
                logger.warning("response missing 'joke' field.")
                return None
            return f"Here's a dad joke:\n{dad_joke}"
        except Exception as e:
            logger.error(f"Api error: {e}", exc_info=True)
            return None

    def _get_advice(self) -> str | None:
        """fetch an advice from the Advice Slip API."""
        logger.info("Trying to an fetch advice...")
        try:
            response = requests.get(self._ADVICE_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Json format: {"slip": {"advice": "..."}}
            advice = data.get('slip', {}).get('advice')
            if not advice:
                logger.warning("response missing 'advice' field.")
            return f"Here's a piece of advice:\n{advice}"
        except Exception as e:
            logger.error(f"Api error: {e}", exc_info=True)

    def _get_joke(self) -> str | None:
        """fetches a single joke from the JokeAPI."""
        logger.info("trying to fetch a joke...")
        try:
            response = requests.get(self._JOKE_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Json format: {"joke": "..."}
            joke = data.get('joke')
            if not joke:
                logger.warning("response missing 'joke' field")
                return None
            return f"Here's a random joke:\n{joke}"
        except Exception as e:
            logger.error(f"JokeAPI Error: {e}", exc_info=True)
            
    def get_random_data(self) -> str | None:
            
            """ method to randomly call any of the 4 API's\n
            this is the only public function, all others are private"""
            logger.info("Deciding Which Api to call")
        
            choice = random.choice([self._get_useless_fact,self._get_dad_joke,self._get_advice,self._get_joke])
            return choice()