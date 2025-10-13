from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from console_manager import console_class
## our main package

console = Console()
title_text = Text()
# Create a single Text object for the full header
header_text = Text()
# PyTransNote in three colors
header_text.append("Py", style="bold magenta")
header_text.append("Trans", style="bold cyan")
header_text.append("Note", style="bold yellow")
# Add a separator and CLI Translator in matching mild colors
header_text.append("  |  CLI Translator", style="bold bright_cyan")

# Print in a single panel, centered
console.print(Panel(header_text, border_style="magenta", expand=False), justify="center")


# Welcome block
welcome_text = Text()
welcome_text.append("🚀 Welcome to PyTransNote! 🚀\n", style="bold yellow")
welcome_text.append("Your Python CLI Translator with deep_translator support.\n", style="bold white")
welcome_text.append("Enjoy translating text across multiple languages easily!", style="bold white")
console.print(Panel(welcome_text, style="bold blue", border_style="cyan"))

# our features
console.print("[bold green]Features:[/bold green]")
console.print("• Uses deep_translator for accurate translations")
console.print("• Maintains translation history automatically")
console.print("• Supports multiple languages: English, Spanish, French, German, etc.")
console.print("• Lightweight and easy to use")
console.print("• Session history saved automatically at program end\n")

## ----------------------

console.print(Panel("Let's start translating! 🚀", style="bold white on blue", expand=False))
console.print("\n")

## main console object
my_console=console_class()

my_console.enter_user_name()

## main console object
while True:
    console.print("\n[bold cyan]--- PyTransNote Main Menu ---\nDo Configure the languages Before using, the Default is English To Spanish[/bold cyan]")
    console.print("1. Translate New Text")
    console.print("2. Configure Languages")
    console.print("3. Delete a Specific Translation")
    console.print("4. View Translation History")
    console.print("5. Clear All History")
    console.print("6. Exit")

    choice = console.input("\n[bold yellow]Enter your choice (1-6): [/bold yellow]").strip()

    if choice == "1":
        my_console.do_translation()

    elif choice == "2":
        # Configure source and target languages
        my_console.from_to_lang()
        my_console.enter_to_lang()

    elif choice == "3":
        my_console.delete_translation()

    elif choice == "4":
        my_console.view_full_history()

    elif choice == "5":
        # Assuming you have a method to clear all history
        my_console.clear_history()

    elif choice == "6":
        # Save history before exiting
        console.print("[bold green]Exiting PyTransNote. Goodbye![/bold green]")
        my_console.hist_file.save_data()
        break
    else:
        console.print("[bold red]Invalid choice. Please enter a number between 1 and 6.[/bold red]")

