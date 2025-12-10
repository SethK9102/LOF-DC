import random
from rich.console import Console
import os
import time
from Entity import Entity

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

class Enemy(Entity):
    def __init__(self, name='Dorian',health=100, strength=20, defense=15, m_defense=15, speed=10, luck=7, attack_type="Physical", exp=0, lvl=1, gold=0, floors={}):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.dead = False
        self.console = Console()
        self.floors = floors
    
    def create_enemies(self):
        enemy_dict = {
            'goblin': Enemy(name="Goblin", health=80, strength=15, defense=10, m_defense=5, speed=12, luck=5, attack_type="Physical", exp=20, lvl=1, gold=15, floors={1,2}),
            "orc": Enemy(name="Orc", health=120, strength=25, defense=20, m_defense=10, speed=8, luck=4, attack_type="Physical", exp=40, lvl=2, gold=30, floors={2,3}),
            "troll": Enemy(name="Troll", health=200, strength=30, defense=25, m_defense=15, speed=6, luck=3, attack_type="Physical", exp=60, lvl=3, gold=50, floors={3,4}),
            "skele wiz": Enemy(name="Skeleton Mage", health=70, strength=10, defense=8, m_defense=20, speed=10, luck=6, attack_type="Magical", exp=50, lvl=2, gold=40, floors={2,3}),
            "DK": Enemy(name="Dark Knight", health=150, strength=35, defense=30, m_defense=20, speed=7, luck=5, attack_type="Physical", exp=80, lvl=4, gold=70, floors={4,5}),
            "fire el": Enemy(name="Fire Elemental", health=100, strength=20, defense=15, m_defense=25, speed=9, luck=4, attack_type="Magical", exp=70, lvl=3, gold=60, floors={3,4}),
            "ice el": Enemy(name="Ice Elemental", health=100, strength=18, defense=15, m_defense=30, speed=9, luck=4, attack_type="Magical", exp=70, lvl=3, gold=60, floors={3,4}),
            "shadow fiend": Enemy(name="Shadow Fiend", health=180, strength=28, defense=22, m_defense=18, speed=11, luck=6, attack_type="Physical", exp=90, lvl=4, gold=80, floors={4,5}),
            "dragon": Enemy(name="Dragon", health=300, strength=50, defense=40, m_defense=35, speed=15, luck=8, attack_type="Physical", exp=150, lvl=5, gold=150, floors={5})

        }

        return enemy_dict
