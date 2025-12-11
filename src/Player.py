from Entity import Entity
from main import print
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
        print("[bold green]Welcome to Legends of Fantasy: Dungeon Crawler![/bold green]")
        self.name = input("Enter your character's name: ")
        wait(0.5)
        print(f"\nHello, [bold blue]{self.name}[/bold blue]! Let's choose your class.")
        wait(1)
        return self.get_class()
    
    def get_class(self):
        clear()
        print("[bold green]Choose your class:[/bold green]" \
        "\n1. Warrior\n2. Mage\n3. Rogue\n4. Giant\n5. Thief")
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
            print("[bold yellow]Your inventory is empty.[/bold yellow]")
        else:
            print("[bold green]Your Inventory:[/bold green]")
            for item_name, item in self.inventory.items():
                if item.type == "Weapon":
                    print(f"[bold green]Equipped Weapon:[/bold green] [bold cyan]{item_name}[/bold cyan]" f"(Strength Increase: [bold magenta]{item.value}[/bold magenta])")
                elif item.type == "Armor":
                    print(f"[bold green]Equipped Armor:[/bold green] [bold cyan]{item_name}[/bold cyan]" f"(Defense Increase: [bold magenta]{item.value}[/bold magenta])")
                elif item.type == "Consumable":
                    consumable_list.append((item, item_name))
            if consumable_list:
                print("\n[bold green]Consumables:[/bold green]")
                for item, item_name in consumable_list:
                    print(f"- [bold cyan]{item_name}[/bold cyan]" f"(Type: [bold magenta]{item.type}[/bold magenta])")
            for item_name, item in self.inventory.items():
                if item.type == "Key Item":
                    key_list.append((item, item_name))
            if key_list:
                print("\n[bold green]Key Items:[/bold green]")
                for item, item_name in key_list:
                    print(f"- [bold cyan]{item_name}[/bold cyan]" f"(Type: [bold magenta]{item.type}[/bold magenta])")
        input("\nPress Enter to continue...")

    def add_item(self, item):
        count = 0
        match item.type:
            case "Weapon":
                for i in self.inventory.values():
                    if i.type == "Weapon" and i.name == item.name:
                        print(f"[bold yellow]You already have this weapon:[/bold yellow] {item.name}")
                        return
                    elif i.type == "Weapon":
                        count += 1
                if count >= 1:
                    print(f"[bold yellow]You can only equip one weapon at a time. Replace your current weapon?[/bold yellow] (y/n)")
                    choice = input().lower()
                    if choice == 'y':
                        self.inventory[i.name] = item
                        self.strength -= self.inventory[i.name].value
                        self.strength += item.value
                        self.equipped[i.name] = item
                        print(f"[bold green]You have equipped:[/bold green] {item.name}")
                else:
                    self.strength += item.value
                    self.equipped[item.name] = item
                    self.inventory[item.name] = item
                    print(f"[bold green]You have equipped:[/bold green] {item.name}")
            case "Armor":
                for i in self.inventory.values():
                    if i.type == "Armor" and i.name == item.name:
                        print(f"[bold yellow]You already have this armor:[/bold yellow] {item.name}")
                        return
                    elif i.type == "Armor":
                        count += 1
                if count >= 1:
                    print(f"[bold yellow]You can only equip one armor at a time. Replace your current armor?[/bold yellow] (y/n)")
                    choice = input().lower()
                    if choice == 'y':
                        self.defense -= self.inventory[i.name].value
                        self.defense += item.value
                        self.equipped[item.name] = item
                        self.inventory[item.name] = item
                        self.inventory.pop(i.name)
                        print(f"[bold green]You have equipped:[/bold green] {item.name}")
                else:
                    self.defense += item.value
                    self.equipped[item.name] = item
                    self.inventory[item.name] = item
                    print(f"[bold green]You have equipped:[/bold green] {item.name}")
            case "Consumable":
                for i in self.inventory.values():
                    if i.type == "Consumable":
                        count += 1
                if count >= 5:
                    print(f"[bold yellow]You can only use five consumables at a time. Discard an existing consumable to add this one?[/bold yellow] (y/n)")
                    choice = input().lower()
                    if choice == 'y':
                        print("Which consumable would you like to discard?")
                        for i in self.inventory.values():
                            if i.type == "Consumable":
                                print(f"- [bold cyan]{i.name}[/bold cyan]")
                        discard_choice = input("Enter the name of the consumable to discard: ")
                        if discard_choice in self.inventory:
                            self.inventory.pop(discard_choice)
                            print(f"[bold green]You have discarded:[/bold green] {discard_choice}")
                        self.inventory[item.name] = item
                else:
                    self.inventory[item.name] = item
                    print(f"[bold green]You have added a consumable:[/bold green] {item.name}")
            case "Key Item":
                self.inventory[item.name] = item
                print(f"[bold green]You have added a key item:[/bold green] {item.name}")
            case _:
                print(f"[bold red]Unknown item type:[/bold red] {item.type}")



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
print(f"Character Created: {player.name}, the {player.class_type}")
print(player.stats_info())
player.inventory_print()

