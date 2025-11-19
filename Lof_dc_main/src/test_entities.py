from entities import Entity, Player, Warrior, Mage, Rogue, Theif, Giant
import pytest
from items import Weapon, Armor


def test_entity_initialization_and_getters():
	e = Entity("E", 100, 10, 5, 0, 0, 0, 0)
	assert e.get_name() == "E"
	assert e.get_health() == 100
	assert e.get_max_health() == 100
	assert e.get_attack() == 10
	assert e.get_defense() == 5
	assert e.get_experiance() == 0
	assert e.get_gold() == 0
	assert e.get_luck() == 0
	assert e.get_speed() == 0


def test_take_damage_and_is_alive():
	e = Entity("Foe", 50, 0, 0, 0, 0, 0, 0)
	e.take_damage(20)
	assert e.get_health() == 30
	assert e.is_alive()
	# damage exceeding current health should floor at 0
	e.take_damage(50)
	assert e.get_health() == 0
	assert not e.is_alive()


def test_heal_and_max_health():
	e = Entity("Healee", 100, 0, 0, 0, 0, 0, 0)
	# reduce health then heal
	e.take_damage(60)
	assert e.get_health() == 40
	e.heal(30)
	assert e.get_health() == 70
	# healing beyond max should clamp to max_health
	e.heal(1000)
	assert e.get_health() == e.get_max_health() == 100


def test_player_weapon_armor_and_inventory():
	# Create a Player with explicit stats
	p = Player("Hero", health=100, attack=10, defense=5, experiance=0, gold=0, luck=0, speed=0)

	# Create weapon and armor and verify set_weapon/set_armor adjust stats
	w = Weapon("Sword", 5, "Sharp", 7)
	a = Armor("Plate", 10, "Heavy", 3)

	base_attack = p.get_attack()
	base_defense = p.get_defense()

	p.set_weapon(w)
	assert p.get_attack() == base_attack + w.get_attack()

	p.set_armor(a)
	assert p.get_defense() == base_defense + a.get_defense()

	# inventory operations
	p.add_to_inventory(w)
	assert w in p.get_inventory()

	# switching weapon should update attack correctly
	w2 = Weapon("Axe", 8, "Chop", 10)
	p.set_weapon(w2)
	assert p.get_attack() == base_attack + w2.get_attack()

