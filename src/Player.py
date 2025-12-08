from src.Entity import Entity

class Player(Entity):
    def __init__(self, name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold=0):
        super().__init__(name, health, strength, defense, m_defense, speed, luck, attack_type, exp, lvl, gold)
        self.position = [0, 0]
        
