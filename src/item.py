from main import rprint
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
        rprint(f"Item Information:\n"
               f"Name: {self.name}\n"
               f"Type: {self.type}\n"
               f"Gold Value: {self.gold}\n"
               f"Effect Value: {self.value}\n"
               f"Floors: {', '.join(map(str, self.floors))}", delay=0.03, style="bold yellow")


