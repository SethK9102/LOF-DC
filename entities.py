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
    

    

    