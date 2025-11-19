import builtins
import types
import random
import pytest

from entities import Warrior, Giant
import Lof_dc_main.src.fighting as fighting_mod
from items import Items


class DummyItem(Items):
    def __init__(self, name="Dummy", cost=0, description=""):
        super().__init__(name, cost, description)
        self.used = False

    def use_item(self, user, target=None):
        # mark that item was used and attach a marker to the user
        self.used = True
        try:
            user.item_used = True
        except Exception:
            pass
        # attempt to remove self from the user's inventory to model consumption
        try:
            inv = user.get_inventory()
            inv.remove(self)
        except Exception:
            try:
                user.inventory.remove(self)
            except Exception:
                pass
        return {"handled": True, "message": f"{self.name} used"}


def _patch_input(monkeypatch, responses):
    """Patch builtins.input to return values from responses sequentially."""
    it = iter(responses)

    def fake_input(prompt=""):
        try:
            return next(it)
        except StopIteration:
            # If no more responses, raise to avoid infinite loops
            raise EOFError("No more input")

    monkeypatch.setattr(builtins, "input", fake_input)


def _patch_random(monkeypatch, uniform_val=1.0, random_val=1.0):
    monkeypatch.setattr(random, "uniform", lambda a, b: uniform_val)
    monkeypatch.setattr(random, "random", lambda: random_val)


def _patch_wait_clear(monkeypatch):
    # disable sleep and clear
    monkeypatch.setattr(fighting_mod, "wait", lambda s: None)
    monkeypatch.setattr(fighting_mod, "clear", lambda x: None)


def test_attack_kills_enemy(monkeypatch):
    # Player attacks and should kill a low-health enemy
    p = Warrior("Att")
    e = Giant("Def")
    e.health = 5

    _patch_wait_clear(monkeypatch)
    _patch_random(monkeypatch, uniform_val=1.0, random_val=1.0)

    # choose action '1' (attack) once
    _patch_input(monkeypatch, ["1"])

    f = fighting_mod.Fighting(p, e)
    f.main_fight()

    assert not e.is_alive()


def test_run_success(monkeypatch):
    p = Warrior("Att")
    e = Giant("Def")

    _patch_wait_clear(monkeypatch)
    # make run always succeed (random -> 0.0)
    _patch_random(monkeypatch, uniform_val=1.0, random_val=0.0)

    # choose action '2' (run)
    _patch_input(monkeypatch, ["2"])

    f = fighting_mod.Fighting(p, e)
    res = f.main_fight()

    assert isinstance(res, dict) and res.get("result") == "ran"


def test_use_item_invokes_use_item_and_consumes(monkeypatch):
    p = Warrior("Att")
    e = Giant("Def")

    # put a dummy item into player's inventory
    item = DummyItem("TestPotion")
    p.add_to_inventory(item)

    _patch_wait_clear(monkeypatch)
    _patch_random(monkeypatch, uniform_val=1.0, random_val=0.0)

    # choose action '3' then select index '1' (use item, 1-based) then '2' to run away
    _patch_input(monkeypatch, ["3", "1", "2"])

    f = fighting_mod.Fighting(p, e)
    res = f.main_fight()

    # item should have been used and removed from inventory
    assert getattr(item, "used") is True
    assert getattr(p, "item_used", False) is True
    # Ensure inventory no longer contains the item
    inv = p.get_inventory()
    assert all(getattr(i, "name", None) != "TestPotion" for i in inv)
    assert isinstance(res, dict) and res.get("result") == "ran"
