
from deep_translator import GoogleTranslator
## we have an lot of option to import for us 
## 1)MyMemoryTranslator: API with a generous free tier that doesn't require a key.
## 2)GoogleTranslator: Google high-quality engine but web scraping (unofficial)
## 3)DeepLTranslator: a free API key (with credit card verification).very high quality translations.
## 4) LibreTranslator: open-source translation engine. we can use their public api instance without a key, but it's better with one



# 1. The text and languages for our test
text_to_translate = "The quick brown fox jumps over the lazy dog."
source_lang = "english"
target_lang = "french"
ts= GoogleTranslator(source='english', target='french')
text_to_translate = "This is a test."

try:
    translated_text = ts.translate(text_to_translate)
    print(f"Translated with {ts.__class__.__name__}:")
    print(translated_text)
except Exception as e:
    print(f"An error occurred: {e}")