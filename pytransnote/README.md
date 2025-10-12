## 🔌 Switchable Translation Engines

This project is designed to be engine-agnostic. The core CRUD logic is separate from the translation service, making it easy to swap between different backends. The `deep-translator` library supports several, including:

-   **MyMemoryTranslator:** A legitimate free-tier API. Can be used anonymously with a daily limit, or with a free API key (via email sign-up) for a **significantly higher limit**.
-   **GoogleTranslator:** Uses Google's engine via web scraping. High quality, but can be unreliable and may break.
-   **LibreTranslator:** A free and open-source translation engine that does not require an API key.
-   **DeepLTranslator:** A premium-quality engine that requires a free API key (with credit card verification).

You can easily switch the engine by changing just a few lines of code in the application.

### Example: How to Swap

```python
# To switch engines, just comment and uncomment the desired section.

# --- Option 1: MyMemory (Anonymous - Easiest Start, Lower Limit) ---
from deep_translator import MyMemoryTranslator
translator = MyMemoryTranslator(source='english', target='french')

# --- Option 2: Google (Anonymous, Unreliable Scraper) ---
# from deep_translator import GoogleTranslator
# translator = GoogleTranslator(source='english', target='french')

# --- Option 3: LibreTranslate (Anonymous, Open-Source) ---
# from deep_translator import LibreTranslator
# translator = LibreTranslator(source='en', target='fr')

# --- Option 4: MyMemory (With API Key - Higher Limit) ---
# from deep_translator import MyMemoryTranslator
# my_api_key = "YOUR_MYMEMORY_KEY_HERE"
# translator = MyMemoryTranslator(api_key=my_api_key, source='english', target='french')

# --- Option 5: DeepL (With API Key - Highest Quality) ---
# from deep_translator import DeepLTranslator
# my_deepl_key = "YOUR_DEEPL_KEY_HERE" 
# translator = DeepLTranslator(api_key=my_deepl_key, source='en', target='fr', use_free_api=True)


# =======================================================
# The rest of your code that calls `translator.translate()` stays the same!
# =======================================================
```