# PyTransNote — CLI Translation Manager

A command-line CRUD application for translating text and managing a persistent translation history. Built with a multi-tier MVC architecture focused on clean code, separation of concerns, and robust error handling.

---

## Features

- **Full CRUD** — Create translations, read full history, delete specific or all entries
- **Persistent Storage** — Translations are saved to a hidden `.history.json` file and persist across sessions
- **Unique ID System** — Each entry gets a permanent ID that is never reused, even after deletion
- **Polished CLI** — Colored feedback and formatted tables powered by `rich`
- **Multi-Language Support** — Translates between all languages supported by the active backend engine

---

## Architecture

**MVC Pattern:**
- **Model / Services** (`history_manager.py`, `manager.py`) — Business logic and data management, fully decoupled from the UI
- **View** (`console_view.py`) — Handles all user interaction (`print` / `input`), receives data from the Controller
- **Controller** (`main.py`) — Orchestrates data flow between Model and View

**Other Design Decisions:**
- Classes follow the Single Responsibility Principle
- JSON file I/O uses explicit `utf-8` encoding for full Unicode support
- `try-except` blocks handle file errors, input conversion failures, and API issues (network failures, rate limits)
- `tests/` directory included for unit testing core business logic

---

## Tech Stack

- **Python 3**
- `deep-translator` — Translation API integration
- `rich` — CLI formatting and tables

---

## Getting Started

**Prerequisites:** Python 3.8+, Git

```bash
# Clone and navigate
git clone git@github.com:Shubhtistic/Python_Projects.git
cd pytransnote

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Run the app:**
```bash
python3 pytransnote/main.py
```

---

## Switchable Translation Engines

The translation engine is decoupled from the core CRUD logic, making it straightforward to swap backends. Supported engines via `deep-translator`:

| Engine | Auth Required | Notes |
|---|---|---|
| `MyMemoryTranslator` | No (or API key for higher limits) | Current default |
| `GoogleTranslator` | No | Scraper-based, can be unreliable |
| `LibreTranslator` | No | Open-source, self-hostable |
| `DeepLTranslator` | API key (free tier available) | Highest quality |

**Switching engines requires changing only a few lines in the source:**

```python
# Option 1: MyMemory — Anonymous (current default)
from deep_translator import MyMemoryTranslator
translator = MyMemoryTranslator(source='english', target='french')

# Option 2: Google — Anonymous scraper
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='english', target='french')

# Option 3: LibreTranslate — Open-source
from deep_translator import LibreTranslator
translator = LibreTranslator(source='en', target='fr')

# Option 4: MyMemory — With API key
from deep_translator import MyMemoryTranslator
translator = MyMemoryTranslator(api_key="YOUR_KEY", source='english', target='french')

# Option 5: DeepL — With API key
from deep_translator import DeepLTranslator
translator = DeepLTranslator(api_key="YOUR_KEY", source='en', target='fr', use_free_api=True)

# The translator.translate() call remains the same across all engines.
```