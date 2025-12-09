from Entity import Entity
from rich.console import Console
import os
import time

wait = time.sleep
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Player(Entity):
    def __init__(self, name, health=100, strength=20, defense=15, m_defense=15, speed=10, luck=7, attack_type="Physical", exp=0, lvl=1, gold=0, inventory={}, equipped={}, floor=0):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold, inventory, equipped, floor)
        self.position = [0, 0]
        self.UID = None
        self.console = Console()
    
    def new_player(self):
        clear()
        self.console.print("[bold green]Welcome to Legends of Fantasy: Dungeon Crawler![/bold green]")
        self.name = input("Enter your character's name: ")
        wait(0.5)
        self.console.print(f"\nHello, [bold blue]{self.name}[/bold blue]! Let's choose your class.")
        wait(1)
        return self.get_class()
    
    def get_class(self):
        clear()
        self.console.print("[bold green]Choose your class:[/bold green]" \
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