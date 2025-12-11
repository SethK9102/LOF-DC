import time
import os
from rich.console import Console
from Player import Player, Warrior, Mage, Rogue, Giant, Thief

console = Console()
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

# player = Warrior("Arin", 87, 30, 20, 10, 12, 7, "Physical", 0, 5, 42)

def header(player):
    # Ominous, unified color theme (deep blue/purple/gray)
    border = "[bold dark_slate_blue]===============================================[/bold dark_slate_blue]"
    title = "[bold medium_purple]      Legend of Fantasy: The Dark Descent      [/bold medium_purple]"
    console.print(border, highlight=False)
    console.print(title, highlight=False)
    console.print(border, highlight=False)
    # Player stats row (cool, muted tones)
    health = f"[bold slate_blue]♥ {player.health}/{player.max_health}[/bold slate_blue]"
    gold = f"[bold gray]⛃ {player.gold}[/bold gray]"
    lvl = f"[bold medium_purple]Lvl {player.lvl}[/bold medium_purple]"
    name_class = f"[bold white]{player.name}[/bold white] the [bold dark_slate_blue]{getattr(player, 'class_type', 'Adventurer')}[/bold dark_slate_blue]"
    stats_line = f"{health}   {gold}   {lvl}   {name_class}"
    console.print(stats_line, style="", highlight=False)
    console.print("[bold dark_slate_blue]-----------------------------------------------[/bold dark_slate_blue]", highlight=False)

def type_out(*args, delay=0.03, **kwargs):
    text = " ".join(str(arg) for arg in args)  # combine all arguments like print does
    for char in text:
        console.print(char, end="", **kwargs)  # preserve style/color if passed
        time.sleep(delay)
    console.print()  # move to new line

rprint = type_out

clear()

rprint("Hello World!", delay=0.1, style="bold medium_purple")
