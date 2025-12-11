import random
from main import rprint
import os
import time
from Entity import Entity

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

class Enemy(Entity):
    def __init__(self, name='Dorian',health=100, strength=20, defense=15, m_defense=15, speed=10, luck=7, attack_type="Physical", exp=0, lvl=1, gold=0, floors=[]):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.dead = False
        self.floors = floors
    
    def create_enemies(self):
        enemy_dict = {
        # ========== FLOOR 1 ==========
            "Cave_Rat": Enemy("Cave Rat", 18, 4, 2, 1, 6, 3, "physical", 6, 1, 3, [1]),
            "Stone_Bug": Enemy("Stone Bug", 25, 5, 5, 2, 4, 1, "physical", 10, 1, 4, [1]),
            "Dust_Spirit": Enemy("Dust Spirit", 20, 3, 1, 3, 8, 5, "magic", 8, 1, 5, [1]),
            "Tunnel_Serpent": Enemy("Tunnel Serpent", 28, 6, 3, 1, 7, 4, "physical", 12, 2, 6, [1]),

            # ========== FLOOR 2 ==========
            "Shadow_Mite": Enemy("Shadow Mite", 20, 6, 2, 4, 10, 5, "magic", 12, 2, 5, [2]),
            "Torch_Spirit": Enemy("Torch Spirit", 32, 7, 3, 3, 8, 4, "magic", 18, 3, 7, [2]),
            "Bone_Picker": Enemy("Bone Picker", 30, 8, 4, 2, 9, 5, "physical", 16, 3, 8, [2]),
            "Ashling": Enemy("Ashling", 26, 5, 2, 5, 11, 3, "magic", 14, 2, 6, [2]),

            # ========== FLOOR 3 ==========
            "Crypt_Guardian": Enemy("Crypt Guardian", 45, 10, 8, 6, 5, 2, "physical", 25, 4, 12, [3]),
            "Magma_Slug": Enemy("Magma Slug", 60, 11, 6, 8, 4, 2, "magic", 32, 4, 14, [3]),
            "Burrowing_Horror": Enemy("Burrowing Horror", 52, 12, 5, 4, 8, 4, "physical", 28, 3, 13, [3]),
            "Soul_Maggot": Enemy("Soul Maggot", 38, 8, 3, 6, 12, 6, "magic", 21, 3, 9, [3]),

            # ========== FLOOR 4 ==========
            "Arcane_Apparition": Enemy("Arcane Apparition", 55, 8, 3, 12, 11, 6, "magic", 40, 5, 20, [4]),
            "Clockwork_Sentinel": Enemy("Clockwork Sentinel", 70, 14, 10, 6, 6, 3, "physical", 48, 6, 25, [4]),
            "Gearling": Enemy("Gearling", 48, 10, 7, 4, 9, 5, "physical", 34, 5, 16, [4]),
            "Mana_Spike": Enemy("Mana Spike", 46, 7, 4, 10, 13, 7, "magic", 38, 5, 18, [4]),

            # ========== FLOOR 5 ==========
            "Mirror_Wraith": Enemy("Mirror Wraith", 62, 12, 5, 14, 15, 8, "magic", 55, 6, 28, [5]),
            "Obsidian_Horror": Enemy("Obsidian Horror", 85, 18, 14, 10, 7, 2, "physical", 75, 7, 33, [5]),
            "Cryst_Fiend": Enemy("Cryst Fiend", 70, 15, 9, 12, 8, 4, "magic", 60, 6, 26, [5]),
            "Shardling": Enemy("Shardling", 58, 13, 6, 8, 14, 6, "physical", 52, 6, 21, [5]),

            # ========== FLOOR 6 ==========
            "Mana_Eater": Enemy("Mana Eater", 92, 15, 8, 18, 12, 9, "magic", 90, 7, 40, [6]),
            "Sentinel_Eye": Enemy("Sentinel Eye", 100, 20, 12, 16, 9, 4, "magic", 120, 8, 50, [6]),
            "Gloom_Roamer": Enemy("Gloom Roamer", 96, 17, 10, 11, 11, 7, "physical", 110, 7, 44, [6]),
            "Hex_Swarm": Enemy("Hex Swarm", 88, 14, 7, 20, 15, 10, "magic", 105, 7, 42, [6]),

            # ========== FLOOR 7 ==========
            "Labyrinth_Fiend": Enemy("Labyrinth Fiend", 110, 22, 18, 10, 10, 5, "physical", 135, 9, 65, [7]),
            "Void_Walker": Enemy("Void Walker", 130, 25, 14, 20, 14, 8, "magic", 160, 10, 80, [7]),
            "Hollow_Sentry": Enemy("Hollow Sentry", 120, 20, 16, 12, 11, 6, "physical", 145, 9, 60, [7]),
            "Eclipse_Shade": Enemy("Eclipse Shade", 108, 18, 10, 22, 17, 9, "magic", 150, 9, 72, [7]),

            # ========== FLOOR 8 ==========
            "Abyss_Knight": Enemy("Abyss Knight", 150, 30, 22, 16, 11, 6, "physical", 190, 11, 100, [8]),
            "Underdepth_Reaver": Enemy("Underdepth Reaver", 165, 32, 20, 20, 13, 7, "physical", 210, 12, 120, [8]),
            "Netherborn": Enemy("Netherborn", 140, 26, 12, 24, 16, 10, "magic", 185, 11, 95, [8]),
            "Abyssal_Seer": Enemy("Abyssal Seer", 135, 21, 15, 28, 18, 12, "magic", 200, 12, 110, [8]),
    }


        return enemy_dict
