

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

    def stats_info(self):
        return f"Name: {self.name}\nLevel: {self.lvl}\nHealth: {self.health}\nStrength: {self.strength}\nDefense: {self.defense}\nMagic Defense: {self.m_defense}\nSpeed: {self.speed}\nLuck: {self.luck}\nExperience: {self.exp}/{self.exp_cap}\nGold: {self.gold}"

