import pytest
from items import Items, Armor, Weapon, Potion, Magic, Special



class TestItems:
    
    def test_items_initialization(self):
        item = Items(name="Health Potion", cost=50, description="Restores 50 HP")
        assert item.get_name() == "Health Potion"
        assert item.get_cost() == 50
        assert item.get_description() == "Restores 50 HP"
    
    def test_armor_initialization(self):
        armor = Armor(name="Steel Armor", cost=200, description="Provides strong defense", defense=15, floors_available=[1, 2, 3])
        assert armor.get_name() == "Steel Armor"
        assert armor.get_cost() == 200
        assert armor.get_description() == "Provides strong defense"
        assert armor.get_defense() == 15
        assert armor.get_floors_available() == [1, 2, 3]
    
    def test_weapon_initialization(self):
        weapon = Weapon(name="Sword", cost=150, description="A sharp blade", attack=20, floors_available=[1, 2])
        assert weapon.get_name() == "Sword"
        assert weapon.get_cost() == 150
        assert weapon.get_description() == "A sharp blade"
        assert weapon.get_attack() == 20
        assert weapon.get_floors_available() == [1, 2]
    
    def test_potion_initialization(self):
        potion = Potion(name="Mana Potion", cost=75, description="Restores 30 MP", effect="Restore 30 MP", floors_available=[1, 2, 3])
        assert potion.get_name() == "Mana Potion"
        assert potion.get_cost() == 75
        assert potion.get_description() == "Restores 30 MP"
        assert potion.get_effect() == "Restore 30 MP"
        assert potion.get_floors_available() == [1, 2, 3]
    
    def test_magic_initialization(self):
        magic = Magic(name="Fireball", cost=120, description="Deals fire damage", spell_power=40, floors_available=[2, 3])
        assert magic.get_name() == "Fireball"
        assert magic.get_cost() == 120
        assert magic.get_description() == "Deals fire damage"
        assert magic.get_spell_power() == 40
        assert magic.get_floors_available() == [2, 3]
    
    def test_special_initialization(self):
        special = Special(name="Invisibility Cloak", cost=300, description="Grants invisibility", unique_ability="Become invisible for 10 seconds", floors_available=[3])
        assert special.get_name() == "Invisibility Cloak"
        assert special.get_cost() == 300
        assert special.get_description() == "Grants invisibility"
        assert special.get_unique_ability() == "Become invisible for 10 seconds"
        assert special.get_floors_available() == [3]
        
    def test_items_without_floors(self):
        armor = Armor(name="Basic Armor", cost=100, description="Basic protection", defense=5)
        assert armor.get_floors_available() is None
        weapon = Weapon(name="Basic Sword", cost=80, description="A simple sword", attack=10)
        assert weapon.get_floors_available() is None
        potion = Potion(name="Small Health Potion", cost=30, description="Restores a small amount of HP", effect="Restore 20 HP")
        assert potion.get_floors_available() is None
        magic = Magic(name="Ice Shard", cost=90, description="Deals ice damage", spell_power=25)
        assert magic.get_floors_available() is None
        special = Special(name="Speed Boots", cost=250, description="Increases speed", unique_ability="Increase speed by 20%")
        assert special.get_floors_available() is None
        
        
class TestArmor(TestItems):
    
    def test_armor_defense(self):
        armor = Armor(name="Chainmail", cost=150, description="Provides moderate defense", defense=10)
        assert armor.get_defense() == 10
    
    def test_armor_floors(self):
        armor = Armor(name="Dragon Scale", cost=500, description="Provides excellent defense", defense=25, floors_available=[5, 6, 7])
        assert armor.get_floors_available() == [5, 6, 7]


class TestWeapon(TestItems):
    
    def test_weapon_attack(self):
        weapon = Weapon(name="Axe", cost=180, description="A heavy axe", attack=30)
        assert weapon.get_attack() == 30
    
    def test_weapon_floors(self):
        weapon = Weapon(name="Magic Wand", cost=220, description="A wand imbued with magic", attack=35, floors_available=[4, 5])
        assert weapon.get_floors_available() == [4, 5]
    
    
class TestPotion(TestItems):
    
    def test_potion_effect(self):
        potion = Potion(name="Stamina Potion", cost=60, description="Restores stamina", effect="Restore 40 Stamina")
        assert potion.get_effect() == "Restore 40 Stamina"
    
    def test_potion_floors(self):
        potion = Potion(name="Elixir", cost=150, description="Restores all stats", effect="Restore all stats to full", floors_available=[2, 3, 4])
        assert potion.get_floors_available() == [2, 3, 4]
        
        
class TestMagic(TestItems):
    
    def test_magic_spell_power(self):
        magic = Magic(name="Lightning Bolt", cost=130, description="Deals lightning damage", spell_power=45)
        assert magic.get_spell_power() == 45
    
    def test_magic_floors(self):
        magic = Magic(name="Earthquake", cost=300, description="Deals earth damage", spell_power=60, floors_available=[6, 7])
        assert magic.get_floors_available() == [6, 7]
        
        
class TestSpecial(TestItems):
    
    def test_special_unique_ability(self):
        special = Special(name="Time Turner", cost=400, description="Manipulates time", unique_ability="Rewind time by 5 seconds")
        assert special.get_unique_ability() == "Rewind time by 5 seconds"
    
    def test_special_floors(self):
        special = Special(name="Phoenix Feather", cost=600, description="Revives upon death", unique_ability="Revive once upon death", floors_available=[8, 9])
        assert special.get_floors_available() == [8, 9]





if __name__ == "__main__":
    pytest.main()