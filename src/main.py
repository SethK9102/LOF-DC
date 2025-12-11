import time
import os
from rich.console import Console

console = Console()
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

def type_out(*args, delay=0.03, **kwargs):
    text = " ".join(str(arg) for arg in args)  # combine all arguments like print does
    for char in text:
        console.print(char, end="", **kwargs)  # preserve style/color if passed
        time.sleep(delay)
    console.print()  # move to new line

print = type_out



