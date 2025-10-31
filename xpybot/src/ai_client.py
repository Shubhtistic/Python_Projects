import google.generativeai as gemini
from . import config
import sys
import google.api_core.exceptions as google_exceptions
import logging

logger = logging.getLogger(__name__)
class AI_Client:
    def __init__(self):
        try:
            if not config.GEMINI_API_KEY:
                raise ValueError("Issue in Loading AI Client API Credentials")
                # if key loaded is loaded properly we will initialze the model
            gemini.configure(api_key=config.GEMINI_API_KEY)
            logger.info("Ai client initialized properly")
        except Exception as e:
            logger.critical(f"Failed to configure Gemini client: {e}", exc_info=True)
            raise ValueError(f"AI Client configuration failed: {e}")
    def ai_reply(self,prompt:str,model: str ="gemini-2.5-flash"):
        logger.info(f"Trying To Send prompt to AI ({model}): '{prompt[:50]}...'")
        try:
            instance=gemini.GenerativeModel(model)
            system_prompt = """You are XpyBot (AI assistant for @XPyBot on Twitter). Goal: Answer user mentions (prompt) **safely, accurately, relevantly, and as concisely as possible** (1-3 Twitter-length sentences). **NEVER use "@" symbol.**
**Critical Rules:**
* **Be:** Friendly, helpful, brief. State name as XpyBot only.
* **Focus:** User mention ONLY.
* **Safety:** NO offensive/hate/sexual/harass/illegal/dangerous content, NO professional advice (finance/legal/medical), NO opinions/emotions. AVOID sensitive topics (politics/religion); decline politely.
* **Privacy:** NO PII (ask/use/reveal).
* **Limitations:** If unclear/unsafe/impossible/opinion-based, **decline politely**. DO NOT invent answers. Stick to public facts.
* **Output:** Plain text, minimal emojis."""

            response = instance.generate_content(
                [system_prompt, prompt] 
            )

            if response.text:
                reply=response.text.strip()
                logger.info("Gemini response received successfully.")
                return reply
            else:
                # is response was empty
                logger.warning("warning, response contained no text.")
                if response.prompt_feedback:
                    logger.warning(f"Reason: {response.prompt_feedback.block_reason}")
                return None
        except google_exceptions.PermissionDenied as e:
            # is permission was denied
            logger.error(f"Gemini API Error, Permission Denied Check your API key {e}", exc_info=True)
            return None
        except google_exceptions.ResourceExhausted as e:
            # rate limit errors
            logger.error(f"Gemini API Error: Rate limit exceeded {e}", exc_info=True)
            return None
        except Exception as e:
            # any other unexpected error
            logger.error(f"Error generating Gemini reply {e}", exc_info=True)
            return None