from dnd import *


def test_roll():
    die = roll(10, 3)
    assert isinstance(die, int)
    assert 3 <= die <= 13


def test_genstats():
    dice = genstats()
    assert len(dice) == 6
    for die in dice:
        assert 3 <= die <= 18
