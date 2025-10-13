# PyTransNote: A Python CLI Translation Manager 🐍

## 📝 Summary
PyTransNote is a robust, command-line CRUD application for translating text and managing a persistent history of all translations. It is built with a professional, multi-tier (Model-View-Controller) architecture that emphasizes clean code, separation of concerns, and robust error handling.

The application uses the `deep-translator` library to interface with free, publicly available translation services and persists all user data locally to a hidden JSON file, correctly handling multi-language (Unicode) characters.

---

## ✨ Key Features
- **Full CRUD Functionality**: **C**reate new translations, **R**ead the full history, and **D**elete specific or all entries.
- **Persistent Storage**: All translations are automatically saved to a hidden `.history.json` file, ensuring user data is never lost between sessions.
- **Unique ID System**: Each translation is assigned a permanent, unique ID that is never reused, even after entries are deleted. This provides a stable and reliable way to reference data.
- **Polished CLI**: A user-friendly and professional command-line interface powered by the `rich` library, featuring colored feedback and beautifully formatted tables.
- **Multi-Language Support**: Capable of translating between a wide variety of languages supported by the chosen backend engine.

---

## 🛠️ Core Concepts & Architecture
This project was architected to demonstrate a strong command of modern Python and professional software design patterns.

- **Model-View-Controller (MVC) Architecture**:
  - **Model/Services (`history_manager.py`, `manager.py`):** The core business logic and data management are fully encapsulated. These components have no knowledge of the user interface.
  - **View (`console_view.py`):** A "dumb" component responsible for all user interaction (`print`/`input`). It takes data from the Controller and displays it.
  - **Controller (`main.py`):** Orchestrates the entire application, managing the flow of data between the Model and the View.
- **Object-Oriented Design (OOP)**: The application is built with distinct classes, each adhering to the **Single Responsibility Principle**.
- **Robust Data & Error Handling**:
  - **File I/O with JSON**: Reads and writes to a JSON file using explicit `utf-8` encoding to fully support international characters.
  - **`try-except` Blocks**: Gracefully handles potential errors from file operations, user input conversion, and external API calls (e.g., network failures, rate limits).
- **Professional Python Tooling**:
  - **Dependency Management**: Uses a project-specific virtual environment (`.venv`) and a `requirements.txt` file.
  - **Testing Structure**: The project is structured with a `tests/` directory to facilitate unit testing of the core business logic.

---

## 💻 Tech Stack
- **Python 3**
- **Libraries:**
  - `deep-translator`: For translation functionality.
  - `rich`: For the polished CLI and table formatting.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git

### Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone git@github.com:shubh4m-2k04/Python_Projects.git
    cd pytransnote
    ```
2.  **Create and activate the virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🎬 Usage
Run the application from the root directory:
```bash
python3 pytransnote/main.py
```

## 🔌 Switchable Translation Engines

This project is designed to be engine-agnostic. The core CRUD logic is separate from the translation service, making it easy to swap between different backends. The `deep-translator` library supports several, including:

-   **MyMemoryTranslator:** A legitimate free-tier API. Can be used anonymously with a daily limit, or with a free API key (via email sign-up) for a **significantly higher limit**.
-   **GoogleTranslator:** Uses Google's engine via web scraping. High quality, but can be unreliable and may break.
-   **LibreTranslator:** A free and open-source translation engine that does not require an API key.
-   **DeepLTranslator:** A premium-quality engine that requires a free API key (with credit card verification).

You can easily switch the engine by changing just a few lines of code in the application.

### Example: How to Swap

```python
# To switch engines, just copy and change appropriate sections in the code

# --- Option 1: MyMemory (Anonymous - Easiest Start, Lower Limit) ---
from deep_translator import MyMemoryTranslator
translator = MyMemoryTranslator(source='english', target='french')
# --- Our Project Currently uses this 

# --- Option 2: Google (Anonymous, Unreliable Scraper) ---
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='english', target='french')

# --- Option 3: LibreTranslate (Anonymous, Open-Source) ---
from deep_translator import LibreTranslator
translator = LibreTranslator(source='en', target='fr')

# --- Option 4: MyMemory (With API Key - Higher Limit) ---
from deep_translator import MyMemoryTranslator
my_api_key = "YOUR_MYMEMORY_KEY_HERE"
translator = MyMemoryTranslator(api_key=my_api_key, source='english', target='french')

# --- Option 5: DeepL (With API Key - Highest Quality) ---
from deep_translator import DeepLTranslator
my_deepl_key = "YOUR_DEEPL_KEY_HERE" 
translator = DeepLTranslator(api_key=my_deepl_key, source='en', target='fr', use_free_api=True)


# =======================================================
# The rest of your code that calls `translator.translate()` stays the same!
# =======================================================
```