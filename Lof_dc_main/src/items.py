class Items():
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description
    
    def use_item(self, user, target=None):
        """Placeholder hook for using an item.

        Subclasses should override this to implement item effects. The method should
        either perform side-effects (e.g., call `user.heal(amount)`) and return a dict
        describing what happened, or return `{"handled": False}` to indicate no action.
        """
        return {"handled": False}
        
    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost
    
    def get_description(self):
        return self.description

class Armor(Items):
    def __init__(self, name, cost, description, defense, floors_available=None):
        super().__init__(name, cost, description)
        self.defense = defense
        self.floors_available = floors_available
        
    def get_defense(self):
        return self.defense
    
    def get_floors_available(self):
        return self.floors_available

class Weapon(Items):
    def __init__(self, name, cost, description, attack, floors_available=None):
        super().__init__(name, cost, description)
        self.attack = attack
        self.floors_available = floors_available
        
    def get_attack(self):
        return self.attack
    
    def get_floors_available(self):
        return self.floors_available

class Potion(Items):
    def __init__(self, name, cost, description, effect, floors_available=None):
        super().__init__(name, cost, description)
        self.effect = effect
        self.floors_available = floors_available
        
    def get_effect(self):
        return self.effect
    
    def get_floors_available(self):
        return self.floors_available

class Magic(Items):
    def __init__(self, name, cost, description, spell_power, floors_available=None):
        super().__init__(name, cost, description)
        self.spell_power = spell_power
        self.floors_available = floors_available
        
    def get_spell_power(self):
        return self.spell_power
    
    def get_floors_available(self):
        return self.floors_available

class Special(Items):
    def __init__(self, name, cost, description, unique_ability, floors_available=None):
        super().__init__(name, cost, description)
        self.unique_ability = unique_ability
        self.floors_available = floors_available

    def get_unique_ability(self):
        return self.unique_ability

    def get_floors_available(self):
        return self.floors_available
    
    
