from manager import my_translator
from rich.console import Console
from rich.panel import Panel

console = Console()

class console_view(my_translator):
    def __init__(self):
        super().__init__()

    available_langs=(
    'english',
    'spanish',
    'french',
    'german',
    'italian',
    'portuguese',
    'dutch',
    'polish',
    'russian',
    'japanese',
    'korean',
    'chinese (simplified)',
    'arabic',
    'turkish',
    'swedish',)

    def enter_user_name(self):
        console.print("[bold cyan]Enter your name:[/bold cyan]", end=" ")
        name=input()
        if not name:
            console.print(Panel(":x: [bold red]No name entered. Defaulting to 'Guest'.[/bold red]", border_style="red"))
        else:
            self.set_user_name(name)
            console.print(Panel(f":white_check_mark: [bold green]Hello, {self.display_user()}![/bold green]", border_style="green"))

    def enter_to_lang(self):
        console.print("[bold cyan]Enter the target language to translate to:[/bold cyan]", end=" ")
        lang = input().strip().lower()  
        if lang in self.available_langs:
            self.set_to_lang(lang)
            console.print(Panel(f":white_check_mark: [bold green]You chose '{lang}' as the source language.[/bold green]", border_style="green"))
        else:
            console.print(Panel(f":x: [bold red]'{lang}' is not a supported language.[/bold red]", border_style="red"))

    def from_to_lang(self):
        console.print("[bold cyan]Enter the source language to translate from:[/bold cyan]", end=" ")
        lang = input().strip().lower()  
        if lang in self.available_langs:
            self.set_from_lang(lang)
            console.print(Panel(f":white_check_mark: [bold green]You chose '{lang}' as the Target language.[/bold green]", border_style="green"))
        else:
            console.print(Panel(f":x: [bold red]'{lang}' is not a supported language.[/bold red]", border_style="red"))

    def do_translation(self):
        console.print("[bold cyan]Enter the sentence to translate:[/bold cyan]", end=" ")
        sentence = input().strip().lower()  
        if not sentence:
            console.print(Panel(":x: [bold red]No text entered. Cannot perform translation.[/bold red]", border_style="red"))
        try:
            console.print(f"[green] {self.translation(sentence)}")
            console.print(Panel(f":white_check_mark: [bold green]Translation Successful![/bold green]\n[bold cyan][/bold cyan]", border_style="green"))
        except Exception as e:
            error_message = """
            [bold red]An error occurred. Sorry about that! :([/bold red]

            [red on yellow]This project uses a free, third-party translation service, which has a daily usage limit.[/red on yellow]

            [red on yellow]A failure can happen for a couple of common reasons:[/red on yellow]
            [red on yellow]- There might be a temporary network issue.[/red on yellow]
            [red on yellow]- The free daily limit for the translation service may have been reached.[/red on yellow]
            """
            console.print(Panel(error_message, border_style="red", title="[bold red]Translation Error[/bold red]"))
            print(e)
