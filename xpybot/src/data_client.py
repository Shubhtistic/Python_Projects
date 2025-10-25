import requests
import random  
import sys    

class Data_Client:

    _FACT_API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"
    _DAD_JOKE_API_URL = "https://icanhazdadjoke.com/"
    _ADVICE_API_URL = "https://api.adviceslip.com/advice"
    
    # --- THIS IS THE FIX ---
    # We added the &blacklistFlags=... parameter to filter out
    # all offensive, political, and religious content.
    _JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?type=single&blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    def __init__(self):
        """Has 4 Apis:
        1)useless fact api 2)Dad jokes api 3)Advice slip api 4) General jokes api\n
        Use get_random_data() method to randomly call any api"""
        print(" Data Client Initilized with 4 apis")

    def _get_useless_fact(self) -> str | None:
        """fetch a useless fact from the useless facts Api\n
        Note: this is an Private function"""
        print("trying to fetch a useless fact...")
        try:
            response = requests.get(self._FACT_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            fact = data.get('text')
            if not fact:
                print("'text' field missing in response", file=sys.stderr)
                return None
            return f"Here's a useless fact:\n{fact}"
        except Exception as e:
            print(f"Api error: {e}", file=sys.stderr)
            return None

    def _get_dad_joke(self) -> str | None:
        """fetches a joke from the dad jokes Api"""
        print("Attempting to fetch a dad joke...")
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
                print("response missing 'joke' field.", file=sys.stderr)
                return None
            return f"Here's a dad joke:\n{dad_joke}"
        except Exception as e:
            print(f"Api error: {e}", file=sys.stderr)
            return None

    def _get_advice(self) -> str | None:
        """fetch an advice from the Advice Slip API."""
        print("Trying to an fetch advice...")
        try:
            response = requests.get(self._ADVICE_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Json format: {"slip": {"advice": "..."}}
            advice = data.get('slip', {}).get('advice')
            if not advice:
                print("response missing 'advice' field.", file=sys.stderr)
                return None
            return advice
        except Exception as e:
            print(f"Api error: {e}", file=sys.stderr)
            return f"Here's a piece of advice:\n{advice}"

    def _get_joke(self) -> str | None:
        """fetches a single joke from the JokeAPI."""
        print("trying to fetch a joke...")
        try:
            response = requests.get(self._JOKE_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Json format: {"joke": "..."}
            joke = data.get('joke')
            if not joke:
                print("response missing 'joke' field", file=sys.stderr)
                return None
            return joke
        except Exception as e:
            print(f"JokeAPI Error: {e}", file=sys.stderr)
            return f"Here's a random joke:\n{joke}"
            
    def get_random_data(self) -> str | None:
            
            """ method to randomly call any of the 4 API's\n
            this is the only public function, all others are private"""
            print("Deciding Which Api to call")
        
            choice = random.randint(1, 4)
            if choice == 1:
                print("Choice (1/4): Useless Fact")
                return self._get_useless_fact()
            elif choice == 2:
                print("Choice (2/4): Dad Joke")
                return self._get_dad_joke()
            elif choice == 3:
                print("Choice (3/4): Advice")
                return self._get_advice()
            else: # Choice is 4
                print("Choice (4/4): General Joke")
                return self._get_joke()
