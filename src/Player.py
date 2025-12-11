from Entity import Entity
from rich.console import Console
console = Console()
def type_out(*args, delay=0.03, **kwargs):
    text = " ".join(str(arg) for arg in args)  # combine all arguments like print does
    for char in text:
        console.print(char, end="", **kwargs)  # preserve style/color if passed
        time.sleep(delay)
    console.print()  # move to new line

rprint = type_out
import os
import time

wait = time.sleep
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Player(Entity):
    def __init__(self, name, health=100, strength=20, defense=15, m_defense=15, speed=10, luck=7, attack_type="Physical", exp=0, lvl=1, gold=0, inventory={}, equipped={}, floor=0):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold, inventory, equipped, floor)
        self.position = [0, 0]
        self.UID = None
    
    def new_player(self):
        clear()
        rprint("Welcome to Legends of Fantasy: Dungeon Crawler!", delay=0.03, style="bold green")
        self.name = input("Enter your character's name: ")
        wait(0.5)
        rprint(f"\nHello, {self.name}! Let's choose your class.", delay=0.03, style="bold blue")
        wait(1)
        return self.get_class()
    
    def get_class(self):
        clear()
        rprint("Choose your class:\n1. Warrior\n2. Mage\n3. Rogue\n4. Giant\n5. Thief", delay=0.03, style="bold green")
        class_choice = input("Enter the number corresponding to your choice: ")
        match class_choice:
            case '1':
                return Warrior(self.name, self.health, self.strength + 10, self.defense + 5, self.m_defense - 10, self.speed - 3, self.luck, self.attack_type, self.exp, self.lvl, self.gold)
            case '2':
                return Mage(self.name, self.health, self.strength + 5, self.defense - 5, self.m_defense + 10, self.speed + 15, self.luck + 5, self.attack_type.replace("Physical", "Magic"), self.exp, self.lvl, self.gold)
            case '3':
                return Rogue(self.name, self.health - 10, self.strength + 5, self.defense - 5, self.m_defense - 5, self.speed + 10, self.luck + 5, self.attack_type, self.exp, self.lvl, self.gold + 20)
            case '4':
                return Giant(self.name, self.health + 50, self.strength + 5, self.defense + 25, self.m_defense - 5, self.speed - 9, self.luck - 3, self.attack_type, self.exp, self.lvl, self.gold)
            case '5':
                return Thief(self.name, self.health - 25, self.strength - 10, self.defense - 10, self.m_defense - 5, self.speed + 10, self.luck + 35, self.attack_type, self.exp, self.lvl, self.gold)
            case _:
                return self.get_class()

    def inventory_print(self):
        clear()
        consumable_list = []
        key_list = []
        if not self.inventory:
            rprint("Your inventory is empty.", delay=0.03, style="bold yellow")
        else:
            rprint("Your Inventory:", delay=0.03, style="bold green")
            for item_name, item in self.inventory.items():
                if item.type == "Weapon":
                    rprint(f"Equipped Weapon: {item_name} (Strength Increase: {item.value})", delay=0.03, style="bold green")
                elif item.type == "Armor":
                    rprint(f"Equipped Armor: {item_name} (Defense Increase: {item.value})", delay=0.03, style="bold green")
                elif item.type == "Consumable":
                    consumable_list.append((item, item_name))
            if consumable_list:
                rprint("\nConsumables:", delay=0.03, style="bold green")
                for item, item_name in consumable_list:
                    rprint(f"- {item_name} (Type: {item.type})", delay=0.03, style="bold cyan")
            for item_name, item in self.inventory.items():
                if item.type == "Key Item":
                    key_list.append((item, item_name))
            if key_list:
                rprint("\nKey Items:", delay=0.03, style="bold green")
                for item, item_name in key_list:
                    rprint(f"- {item_name} (Type: {item.type})", delay=0.03, style="bold cyan")
        input("\nPress Enter to continue...")

    def add_item(self, item):
        count = 0
        match item.type:
            case "Weapon":
                for i in self.inventory.values():
                    if i.type == "Weapon" and i.name == item.name:
                        rprint(f"You already have this weapon: {item.name}", delay=0.03, style="bold yellow")
                        return
                    elif i.type == "Weapon":
                        count += 1
                if count >= 1:
                    rprint("You can only equip one weapon at a time. Replace your current weapon? (y/n)", delay=0.03, style="bold yellow")
                    choice = input().lower()
                    if choice == 'y':
                        self.inventory[i.name] = item
                        self.strength -= self.inventory[i.name].value
                        self.strength += item.value
                        self.equipped[i.name] = item
                        rprint(f"You have equipped: {item.name}", delay=0.03, style="bold green")
                else:
                    self.strength += item.value
                    self.equipped[item.name] = item
                    self.inventory[item.name] = item
                    rprint(f"You have equipped: {item.name}", delay=0.03, style="bold green")
            case "Armor":
                for i in self.inventory.values():
                    if i.type == "Armor" and i.name == item.name:
                        rprint(f"You already have this armor: {item.name}", delay=0.03, style="bold yellow")
                        return
                    elif i.type == "Armor":
                        count += 1
                if count >= 1:
                    rprint("You can only equip one armor at a time. Replace your current armor? (y/n)", delay=0.03, style="bold yellow")
                    choice = input().lower()
                    if choice == 'y':
                        self.defense -= self.inventory[i.name].value
                        self.defense += item.value
                        self.equipped[item.name] = item
                        self.inventory[item.name] = item
                        self.inventory.pop(i.name)
                        rprint(f"You have equipped: {item.name}", delay=0.03, style="bold green")
                else:
                    self.defense += item.value
                    self.equipped[item.name] = item
                    self.inventory[item.name] = item
                    rprint(f"You have equipped: {item.name}", delay=0.03, style="bold green")
            case "Consumable":
                for i in self.inventory.values():
                    if i.type == "Consumable":
                        count += 1
                if count >= 5:
                    rprint("You can only use five consumables at a time. Discard an existing consumable to add this one? (y/n)", delay=0.03, style="bold yellow")
                    choice = input().lower()
                    if choice == 'y':
                        rprint("Which consumable would you like to discard?", delay=0.03, style="bold yellow")
                        for i in self.inventory.values():
                            if i.type == "Consumable":
                                rprint(f"- {i.name}", delay=0.03, style="bold cyan")
                        discard_choice = input("Enter the name of the consumable to discard: ")
                        if discard_choice in self.inventory:
                            self.inventory.pop(discard_choice)
                            rprint(f"You have discarded: {discard_choice}", delay=0.03, style="bold green")
                        self.inventory[item.name] = item
                else:
                    self.inventory[item.name] = item
                    rprint(f"You have added a consumable: {item.name}", delay=0.03, style="bold green")
            case "Key Item":
                self.inventory[item.name] = item
                rprint(f"You have added a key item: {item.name}", delay=0.03, style="bold green")
            case _:
                rprint(f"Unknown item type: {item.type}", delay=0.03, style="bold red")



class Warrior(Player):
    def __init__(self, name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.class_type = "Warrior"



class Mage(Player):
    def __init__(self, name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.class_type = "Mage"



class Rogue(Player):
    def __init__(self, name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.class_type = "Rogue"



class Giant(Player):
    def __init__(self, name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.class_type = "Giant"



class Thief(Player):
    def __init__(self, name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.class_type = "Thief"



test = Player("PlaceHolder")
player = test.new_player()
rprint(f"Character Created: {player.name}, the {player.class_type}")
rprint(player.stats_info())
player.inventory_print()

