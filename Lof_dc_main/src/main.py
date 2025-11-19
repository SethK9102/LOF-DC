import os
import time
import rich
from rich.console import Console
from entities import Entity, Player, Warrior, Mage, Rogue, Theif, Giant
from items import Items, Armor, Weapon, Potion, Magic, Special

rprint = rich.print
clear = os.system
wait = time.sleep
console = Console()

if __name__ == "__main__": 
    console.rule("[bold red]LOF: Dungeon Crawler[/bold red]")


