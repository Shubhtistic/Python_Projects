from manager import my_translator
from rich.console import Console
from rich.panel import Panel
from history_manager import history_manager_class as hist

console = Console()
## instantiate an Console obj from rich Console

class console_view(my_translator):
    def __init__(self):
        super().__init__()
        self.hist_file=hist()
        if(not self.hist_file.read_and_load_data()):
            print("History file not found or was empty!.\nNew one will be created after this session closes containing data of this session")
        self.current_max_id=self.hist_file.max_id+1
        

    available_langs=(
    'english',
    'hindi',
    'marathi',
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
            ts=self.translation(sentence)
            console.print(f"[green] {ts}")
            console.print(Panel(f":white_check_mark: [bold green]Translation Successful![/bold green]\n[bold cyan][/bold cyan]", border_style="green"))
            data_to_dump={
                "ID":self.current_max_id,
                "Base Lang":self.__from_lang,
                "Target Language":self.__to_lang,
                "Translated_String":ts
            }
            self.hist_file.save_data(data_to_dump)
            self.current_max_id+=1
        
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
