import random
import re
from rich.console import Console
console = Console()
import os
import time
clear = os.system
wait = time.sleep


class Fighting:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def effective_attack_value(self, attack: float, defense: float) -> float:
        """Compute an "effective" attack contribution using a rational formula.

        Formula: effective = attack**2 / (attack + defense)

        Rationale:
        - When attack == defense, effective = attack/2.
        - When attack >> defense, effective -> attack (full power).
        - When defense >> attack, effective -> attack**2/defense (strongly reduced).
        This makes both attack and defense important and gives diminishing returns.
        """
        attack = float(max(0.0, attack))
        defense = float(max(0.0, defense))
        if attack + defense == 0:
            return 0.0
        return (attack ** 2) / (attack + defense)

    def compute_damage(self, attack: float, defense: float, *, power: float = 1.0, variance: float = 0.08, crit_chance: float = 0.04, crit_multiplier: float = 1.5, min_damage: int = 0) -> dict:
        """Compute final damage from raw attack and defense values.

        Returns a dict with keys: damage (int), base (float), after_variance (float), is_crit (bool).
        """
        base = self.effective_attack_value(attack, defense) * power
        var_factor = random.uniform(1.0 - variance, 1.0 + variance) if variance > 0 else 1.0
        after_var = base * var_factor
        is_crit = random.random() < crit_chance if crit_chance > 0 else False
        if is_crit:
            after_var *= crit_multiplier

        damage = int(max(min_damage, round(after_var)))
        return {
            "damage": damage,
            "base": base,
            "after_variance": after_var,
            "is_crit": is_crit,
            "var_factor": var_factor,
        }

    def resolve_attack(self, attacker, defender, *, attack_attr_candidates=None, defense_attr_candidates=None, hp_attr_candidates=None, apply_damage=True, compute_kwargs=None) -> dict:
        """Try to resolve an attack between two objects.

        Attempts to read attack/defense/hp from common attributes or getters, computes damage using
        `compute_damage` and optionally applies it to the defender. `compute_kwargs` are forwarded
        to `compute_damage` to enable deterministic testing.
        """
        if attack_attr_candidates is None:
            attack_attr_candidates = ("attack", "atk", "get_attack")
        if defense_attr_candidates is None:
            defense_attr_candidates = ("defense", "def", "get_defense")
        if hp_attr_candidates is None:
            hp_attr_candidates = ("health", "hp", "get_health")

        def _read_stat(obj, candidates):
            for name in candidates:
                if hasattr(obj, name):
                    val = getattr(obj, name)
                    if callable(val):
                        try:
                            return float(val())
                        except Exception:
                            continue
                    try:
                        return float(val)
                    except Exception:
                        continue
            return 0.0

        atk = _read_stat(attacker, attack_attr_candidates)
        dfn = _read_stat(defender, defense_attr_candidates)

        result = self.compute_damage(atk, dfn, **(compute_kwargs or {}))

        if apply_damage:
            dmg = result["damage"]
            if hasattr(defender, "take_damage") and callable(getattr(defender, "take_damage")):
                try:
                    defender.take_damage(dmg)
                except Exception:
                    pass
            else:
                for name in hp_attr_candidates:
                    if hasattr(defender, name):
                        val = getattr(defender, name)
                        try:
                            new_hp = float(val) - dmg
                            if isinstance(val, int):
                                setattr(defender, name, max(0, int(round(new_hp))))
                            else:
                                setattr(defender, name, max(0.0, new_hp))
                        except Exception:
                            continue
                        break

        return {"attacker_attack": atk, "defender_defense": dfn, **result}

    def main_fight(self):
        # Interactive fight loop (player chooses actions each turn)
        while self.player.is_alive() and self.enemy.is_alive():
            clear('cls')
            console.rule(f"[bold red]FIGHT ZONE[/bold red]")
            wait(0.25)
            console.rule(f"[bold blue]A wild {self.enemy.get_name()} appears![/bold blue]")

            # Show status
            try:
                p_hp = self.player.get_health()
                p_max = self.player.get_max_health()
            except Exception:
                p_hp = getattr(self.player, 'health', 0)
                p_max = getattr(self.player, 'max_health', p_hp)
            try:
                e_hp = self.enemy.get_health()
                e_max = self.enemy.get_max_health()
            except Exception:
                e_hp = getattr(self.enemy, 'health', 0)
                e_max = getattr(self.enemy, 'max_health', e_hp)

            console.print(f"[bold green]Player[/bold green]: {p_hp} / {p_max}")
            console.print(f"[bold red]Enemy[/bold red]: {e_hp} / {e_max}\n")

            # Player action selection
            console.print("Choose an action:")
            console.print("1) Attack    2) Run    3) Use Item")
            choice = input("Action (1/2/3): ").strip()

            if choice == "1":
                # Attack
                res = self.resolve_attack(self.player, self.enemy)
                console.print(f"You attack and deal [bold]{res['damage']}[/bold] damage.")
            elif choice == "2":
                # Attempt to run: use speed to influence chance
                try:
                    p_speed = float(self.player.get_speed())
                except Exception:
                    p_speed = float(getattr(self.player, 'speed', 0))
                try:
                    e_speed = float(self.enemy.get_speed())
                except Exception:
                    e_speed = float(getattr(self.enemy, 'speed', 0))
                run_chance = 0.5 + (p_speed - e_speed) / 100.0
                run_chance = max(0.05, min(0.95, run_chance))
                if random.random() < run_chance:
                    console.print("You successfully fled the battle.")
                    return {"result": "ran"}
                else:
                    console.print("You failed to run away!")
            elif choice == "3":
                while True:
                    console.print("You rummage through your inventory to find an item to use.")
                    inventory = self.player.get_inventory()
                    if not inventory:
                        console.print("Your inventory is empty!")
                        continue
                    console.print("Your items:")
                    for idx, item in enumerate(inventory, start=1):
                        console.print(f"{idx}) {item.get_name()}: {item.description}")
                    item_choice = input(f"Select an item to use (1-{len(inventory)}) or 'c' to cancel: ").strip()
                    if item_choice.lower() == 'c':
                        # cancel item selection and return to action selection
                        break
                    try:
                        item_idx = int(item_choice) - 1
                        if item_idx < 0 or item_idx >= len(inventory):
                            console.print("Invalid item selection.")
                            continue
                        item = inventory[item_idx]
                        use_result = item.use_item(self.player, self.enemy)
                        if use_result.get("handled", False):
                            console.print(f"You used {item.get_name()}.")
                            if "message" in use_result:
                                console.print(use_result["message"])
                        else:
                            console.print(f"{item.get_name()} had no effect.")
                        # after an attempt to use an item, return to main action selection
                        break
                    except ValueError:
                        console.print("Invalid input.")
                        continue

            # Check if enemy died from player's action
            if not self.enemy.is_alive():
                console.print(f"[bold green]{self.enemy.get_name()} defeated![/bold green]")
                
                break

            # Enemy's turn (simple AI)
            console.print(f"\n{self.enemy.get_name()} prepares to attack...")
            wait(0.6)
            eres = self.resolve_attack(self.enemy, self.player)
            console.print(f"{self.enemy.get_name()} hits you for [bold]{eres['damage']}[/bold] damage.")

            if not self.player.is_alive():
                console.print("You have been defeated...")
                break
