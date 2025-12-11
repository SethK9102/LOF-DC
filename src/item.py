from main import print
import os
import time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

class Item:
    def __init__(self, name="PlaceHolder", type="Armour", gold=10, value=10, floors={}):
        self.name = name
        self.type = type  
        self.gold = gold
        self.value = value
        self.floors = floors

    def display_info(self):
        clear()
        print(f"[bold yellow]Item Information:[/bold yellow]\n"
                            f"Name: [bold cyan]{self.name}[/bold cyan]\n"
                            f"Type: [bold magenta]{self.type}[/bold magenta]\n"
                            f"Gold Value: [bold green]{self.gold}[/bold green]\n"
                            f"Effect Value: [bold blue]{self.value}[/bold blue]\n"
                            f"Floors: [bold blue]{', '.join(map(str, self.floors))}[/bold blue]")

        
