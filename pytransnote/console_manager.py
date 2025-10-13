from manager import my_translator
from rich.console import Console
from rich.panel import Panel
from history_manager import history_manager_class as hist
from rich.table import Table

console = Console()
## instantiate an Console obj from rich Console

class console_class(my_translator):
    def __init__(self):
        super().__init__()
        self.hist_file=hist()
        
        if(not self.hist_file.read_and_load_data()):
            pass
            # print("History file not found or was empty!.\nNew one will be created after this session closes containing data of this session")
        self.current_max_id=self.hist_file.max_id+1
        self.ids_list=[item.get("ID") for item in self.hist_file.history_list]
        ## we make this in advance for easy lookups later
        ## in this we get all int values mapped to "ID" key 
        ## we did an list comprehension in this step
        ## this list contains all our ids 
        

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
        console.print("[bold cyan]Enter your name/Username:[/bold cyan]", end=" ")
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
            console.print(Panel(f":white_check_mark: [bold green]You chose '{lang}' as the Target language\nNow Lets Try doing an translation maybe.[/bold green]", border_style="green"))
        else:
            console.print(Panel(f":x: [bold red]'{lang}' is not a supported language.[/bold red]", border_style="red"))

    def from_to_lang(self):
        console.print("[bold cyan]Enter the source language to translate from:[/bold cyan]", end=" ")
        lang = input().strip().lower()  
        if lang in self.available_langs:
            self.set_from_lang(lang)
            console.print(Panel(f":white_check_mark: [bold green]You chose '{lang}' as the Source language.[/bold green]", border_style="green"))
        else:
            console.print(Panel(f":x: [bold red]'{lang}' is not a supported language.[/bold red]", border_style="red"))

    def do_translation(self):
        console.print("[bold cyan]Enter the sentence to translate:[/bold cyan]", end=" ")
        sentence = input().strip()
        if not sentence:
            console.print(Panel(":x: [bold red]No text entered. Cannot perform translation.[/bold red]", border_style="red"))
            return
        try:
            ts=self.translation(sentence)
            console.print(f"[green] {ts}")
            console.print(Panel(f":white_check_mark: [bold green]Translation Successful![/bold green]\n[bold cyan][/bold cyan]", border_style="green"))
            data_to_dump={
                "ID":self.current_max_id,
                "Base Language":self._from_lang,
                "Target Language":self._to_lang,
                "Translated Info":ts
            }
            self.hist_file.history_list.append(data_to_dump)
            self.ids_list.append(self.current_max_id)
            self.current_max_id+=1
        
        except Exception as e:
            ## we can use exception object to pinpoimt exact issue
            error_message = """
            [bold red]An error occurred. Sorry about that! :([/bold red]

            [red on yellow]This project uses a free, third-party translation service, which has a daily usage limit.[/red on yellow]

            [red on yellow]A failure can happen for a couple of common reasons:[/red on yellow]
            [red on yellow]- There might be a temporary network issue.[/red on yellow]
            [red on yellow]- The free daily limit for the translation service may have been reached.[/red on yellow]
            """
            console.print(Panel(error_message, border_style="red", title="[bold red]Translation Error[/bold red]"))
            
 ## now our file i/o functions 
    def delete_translation(self):
        if not self.hist_file.history_list:
            console.print(Panel("History is empty.", border_style="red"))
            return
        try:
            target = int(input("Please Enter ID To Delete a Specific Translation: "))
            if target not in self.ids_list:
                console.print(Panel(f"ID {target} not found in history.", border_style="red"))
            else:
                for index, dict_item in enumerate(self.hist_file.history_list):
                    found = dict_item.get("ID")
                    if found == target:
                        del self.hist_file.history_list[index]
                        self.ids_list.remove(found)
                        console.print(Panel(f"ID {target} deleted successfully.", border_style="green"))
                        break
        except ValueError:
            console.print(Panel("Please enter numeric values only.", border_style="red"))



    def view_full_history(self):
        if not self.hist_file.history_list:
            console.print(Panel("No translations to show.", border_style="yellow"))
            return

        table = Table(title="Translation History")

        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Translation", style="green", overflow="fold")
        table.add_column("Base Language", style="magenta")
        table.add_column("Target Language", style="magenta")

        for entry in self.hist_file.history_list:
            table.add_row(
                str(entry.get("ID")),
                entry.get("Translated Info"),
                entry.get("Base Language"),
                entry.get("Target Language")
            )

        console.print(table)

    def clear_history(self):
        console.print(Panel("Are you sure you want to wipe all history (old and new)?", border_style="red"))
        console.print(Panel("Enter 'y' for yes, any other input will cancel.", border_style="yellow"))
        choice = input("Please enter: ").strip().lower()
        if choice == 'y' or choice == 'yes':
            self.hist_file.history_list.clear()
            self.ids_list.clear()
            console.print(Panel("All history cleared successfully.", border_style="green"))
        else:
            console.print(Panel("Exit without clearing history.", border_style="cyan"))

































    # def __del__(self):
    #     # This is our desctructor, auto saves file on closing of program
    #     try:
    #         self.hist_file.save_data()
    #         print("Session history saved successfully.")
    #     except Exception as e:
    #         print(f"Failed to save history: {e}")
    ## we can simply call it in while loop exit also
