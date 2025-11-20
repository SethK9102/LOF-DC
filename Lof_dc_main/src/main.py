import os
import time
import rich
from rich.console import Console
from fighting import Fighting
from entities import Entity, Player, Warrior, Mage, Rogue, Theif, Giant, Enemies
from items import Items, Armor, Weapon, Potion, Magic, Special

rprint = rich.print
clear = os.system
wait = time.sleep
console = Console()

def set_up_enemies():
    enemy_dict = {
        "basic": Enemies()
    }



if __name__ == "__main__": 
    console.rule("[bold red]Legand of Fantasy: The Dark Cavern[/bold red]")


