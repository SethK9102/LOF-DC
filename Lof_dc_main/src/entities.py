from rich.console import Console
console = Console()
import os
import time

class Entity():
    def __init__(self, name, health, attack, defense, experiance, gold, luck, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.experiance = experiance
        self.gold = gold
        self.luck = luck
        self.speed = speed


    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def get_max_health(self):
        return self.max_health
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_experiance(self):
        return self.experiance
    
    def get_gold(self):
        return self.gold
    
    def get_luck(self):
        return self.luck
    
    def get_speed(self):
        return self.speed
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            if self.is_alive():
                return True
            return False
        
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
    

        

class Player(Entity):
    def __init__(self, name, health, attack, defense, experiance, gold, luck, speed):
        super().__init__(name, health, attack, defense, experiance, gold, luck, speed)
        self.level = 1
        self.inventory = []
        self.floor = 0
        self.position = {'x': 0, 'y': 0}
        self.weapon = None
        self.armor = None
    def get_level(self):
        return self.level
    
    def get_inventory(self):
        return self.inventory
    
    def get_floor(self):
        return self.floor
    
    def get_position(self):
        return self.position
    
    def ask_class(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("Choose your class:")
        console.print("1. Warrior")
        console.print("2. Mage")
        console.print("3. Rogue")
        console.print("4. Theif")
        console.print("5. Giant")
        choice = int(input("Enter the number of your choice: ")) if choice in [1, 2, 3, 4, 5] else self.ask_class()
        return choice
    
    def set_weapon(self, weapon):
        self.attack -= self.weapon.get_attack() if self.weapon else 0
        self.weapon = weapon
        self.attack += weapon.get_attack()
        
    def set_armor(self, armor):
        self.defense -= self.armor.get_defense() if self.armor else 0
        self.armor = armor
        self.defense += armor.get_defense()
        
    def add_to_inventory(self, item):
        self.inventory.append(item)

        
    
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, health=140, attack=20, defense=15, experiance=0, gold=0, luck=5, speed=10)
        self.attack_type = "Melee"
        self.class_type = "Warrior"
              
class Mage(Player):
    def __init__(self, name):
        super().__init__(name, health=100, attack=30, defense=10, experiance=0, gold=0, luck=10, speed=15)
        self.attack_type = "Magic"
        self.class_type = "Mage"
        
class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, health=120, attack=25, defense=12, experiance=0, gold=0, luck=15, speed=20)
        self.attack_type = "Stealth"
        self.class_type = "Rogue"
        
class Theif(Player):
    def __init__(self, name):
        super().__init__(name, health=110, attack=22, defense=11, experiance=0, gold=0, luck=20, speed=25)
        self.attack_type = "Steal"
        self.class_type = "Theif"
        
class Giant(Player):
    def __init__(self, name):
        super().__init__(name, health=200, attack=18, defense=20, experiance=0, gold=0, luck=3, speed=8)
        self.attack_type = "Crush"
        self.class_type = "Giant"
    


class Enemies(Entity):
    def __init__(self, name: str = "Enemy", health: int = 100, attack: int = 10, defense: int = 8, experiance: int = 10, gold: int = 15, luck: int = 10, speed: int = 8, floors_avalible: list = [1, 2, 3, 4, 5, 6, 7], discription: str = "Basic Enemy"):
        self.floors_avalible = floors_avalible
        self.discription = discription

    def get_floors_avalible(self):
        return self.floors_avalible
    
    def get_discription(self):
        return self.discription