import google.generativeai as gemini
from . import config
import sys
import google.api_core.exceptions as google_exceptions
class AI_Client:
    def __init__(self):
        try:
            if not config.GEMINI_API_KEY:
                raise ValueError("Issue in Loading AI Client API Credentials")
                # if key loaded is loaded properly we will initialze the model
            gemini.configure(api_key=config.GEMINI_API_KEY)
            print("Ai client initialized properly")
        except Exception as e:
            print(f"CRITICAL ERROR: Failed to configure Gemini client: {e}", file=sys.stderr)
            raise ValueError(f"AI Client configuration failed: {e}")
    def ai_reply(self,prompt:str,model: str ="gemini-2.5-flash"):
        print(f"Trying To Send prompt to AI ({model}): '{prompt[:50]}...'")
        try:
            instance=gemini.GenerativeModel(model)
            system_prompt = "Your Name is XpyBot And are a helpful assistant responding to Twitter mentions."

            response = instance.generate_content(
                [system_prompt, prompt] 
            )

            if response.text:
                reply=response.text.strip()
                print("Gemini response received successfully.")
                return reply
            else:
                # is response was empty
                print("warning, response contained no text.", file=sys.stderr)
                if response.prompt_feedback:
                    print(f"Reason: {response.prompt_feedback.block_reason}", file=sys.stderr)
                return None
        except google_exceptions.PermissionDenied as e:
            # is permission was denied
            print(f"Gemini API Error: Permission Denied. Check your API key. {e}", file=sys.stderr)
            return None
        except google_exceptions.ResourceExhausted as e:
            # rate limit errors
            print(f"Gemini API Error: Rate limit exceeded. {e}", file=sys.stderr)
            return None
        except Exception as e:
            # any other unexpected error
            print(f"Error generating Gemini reply: {e}", file=sys.stderr)
            return None