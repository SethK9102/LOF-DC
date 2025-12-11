import os
import time
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep
from rich.console import Console
console = Console()

def type_out(*args, delay=0.03, **kwargs):
    text = " ".join(str(arg) for arg in args)  # combine all arguments like print does
    for char in text:
        console.print(char, end="", **kwargs)  # preserve style/color if passed
        time.sleep(delay)
    console.print()  # move to new line

rprint = type_out

class Entity:
    def __init__(self, name, health=100, strength=20, defense=15, m_defense=15, speed=10, luck=7, attack_type="Physical", exp=0, lvl=1, gold=0, inventory={}, equipped={}, floor=0):
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength
        self.defense = defense
        self.m_defense = m_defense
        self.speed = speed
        self.luck = luck
        self.attack_type = attack_type
        self.exp = exp
        self.lvl = lvl
        self.gold = gold
        self.inventory = inventory
        self.equipped = equipped
        self.floor = floor
        self.exp_cap = 100

    def is_alive(self):
        return self.health > 0
    
    def level_up(self):
        self.lvl += 1
        self.exp = 0
        self.exp_cap = int(self.exp_cap * 1.2)

    def choose_lvl_up_stat(self):
        clear()
        rprint("Choose a stat to increase:", delay=0.03, style="bold yellow")
        rprint(f"1. Health: Currently {self.health}", delay=0.03, style="bold yellow")
        rprint(f"2. Strength: Currently {self.strength}", delay=0.03, style="bold yellow")
        rprint(f"3. Defense: Currently {self.defense}", delay=0.03, style="bold yellow")
        rprint(f"4. Magic Defense: Currently {self.m_defense}", delay=0.03, style="bold yellow")
        rprint(f"5. Speed: Currently {self.speed}", delay=0.03, style="bold yellow")
        rprint(f"6. Luck: Currently {self.luck}", delay=0.03, style="bold yellow")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            self.health += 10
        elif choice == "2":
            self.strength += 4
        elif choice == "3":
            self.defense += 3
        elif choice == "4":
            self.m_defense += 3
        elif choice == "5":
            self.speed += 5
        elif choice == "6":
            self.luck += 5
        else:
            rprint("Invalid choice.")
            self.choose_lvl_up_stat()


    def stats_info(self):
        return f"Name: {self.name}\nLevel: {self.lvl}\nHealth: {self.health}\nStrength: {self.strength}\nDefense: {self.defense}\nMagic Defense: {self.m_defense}\nSpeed: {self.speed}\nLuck: {self.luck}\nExperience: {self.exp}/{self.exp_cap}\nGold: {self.gold}"

