import pytest
import random
from entities import Player, Warrior, Mage, Rogue, Theif, Giant
from fighting import Fighting


class TestFighting:
    def test_effective_attack_value_equal(self):
        f = Fighting(None, None)
        val = f.effective_attack_value(20, 20)
        assert val == pytest.approx(10.0)

    def test_effective_attack_value_attacker_advantage(self):
        f = Fighting(None, None)
        high = f.effective_attack_value(100, 10)
        med = f.effective_attack_value(50, 10)
        assert high > med

    def test_effective_attack_value_defense_advantage(self):
        f = Fighting(None, None)
        low = f.effective_attack_value(10, 100)
        assert low < 2.0

    def test_compute_damage_deterministic(self):
        f = Fighting(None, None)
        # deterministic: no variance, no crits
        out = f.compute_damage(30, 10, variance=0.0, crit_chance=0.0, power=1.0)
        base = f.effective_attack_value(30, 10)
        assert out["damage"] == round(base)

    def test_resolve_attack_applies_damage(self):
        attacker = Warrior("Att")
        defender = Giant("Def")
        before_hp = defender.get_health()
        f = Fighting(attacker, defender)
        # deterministic compute (no variance, no crits)
        res = f.resolve_attack(attacker, defender, apply_damage=True, compute_kwargs={"variance": 0.0, "crit_chance": 0.0, "power": 1.0})
        expected = f.compute_damage(attacker.get_attack(), defender.get_defense(), variance=0.0, crit_chance=0.0, power=1.0)
        assert res["damage"] == expected["damage"]
        assert defender.get_health() == before_hp - expected["damage"]

    def test_balance_across_classes(self):
        classes = [Warrior, Mage, Rogue, Theif, Giant]
        f = Fighting(None, None)
        for A in classes:
            for B in classes:
                a = A("a")
                b = B("b")
                out1 = f.compute_damage(a.get_attack(), b.get_defense(), variance=0.0, crit_chance=0.0)
                out2 = f.compute_damage(b.get_attack(), a.get_defense(), variance=0.0, crit_chance=0.0)
                # both sides should result in positive integer damage (or zero) and not be extremely lopsided
                d1 = out1["damage"]
                d2 = out2["damage"]
                assert d1 >= 0 and d2 >= 0
                # avoid division by zero
                if d1 == 0 and d2 == 0:
                    continue
                if d1 == 0:
                    ratio = float('inf')
                else:
                    ratio = d2 / d1
                # assert the ratio is within a reasonable bound to indicate balance
                assert (d1 == 0 and d2 >= 0) or (0.2 <= ratio <= 5.0)
