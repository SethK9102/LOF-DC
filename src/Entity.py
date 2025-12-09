from rich.console import Console
import os
import time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

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
        self.console = Console()

    def is_alive(self):
        return self.health > 0
    
    def level_up(self):
        self.lvl += 1
        self.exp = 0
        self.exp_cap = int(self.exp_cap * 1.2)

    def choose_lvl_up_stat(self):
        clear()
        self.console.print("Choose a stat to increase:")
        self.console.print("1. Health")
        self.console.print("2. Strength")
        self.console.print("3. Defense")
        self.console.print("4. Magic Defense")
        self.console.print("5. Speed")
        self.console.print("6. Luck")
        choice = self.console.input("Enter your choice (1-6): ")
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
            self.console.print("Invalid choice.")
            self.choose_lvl_up_stat()


    def stats_info(self):
        return f"Name: {self.name}\nLevel: {self.lvl}\nHealth: {self.health}\nStrength: {self.strength}\nDefense: {self.defense}\nMagic Defense: {self.m_defense}\nSpeed: {self.speed}\nLuck: {self.luck}\nExperience: {self.exp}/{self.exp_cap}\nGold: {self.gold}"

