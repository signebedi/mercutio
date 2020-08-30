import pytest
import mercutio.mercutio as mc

def test_gen():
    player = mc.Player()
    player.gen()

    assert isinstance(player.player_class, (str))
    assert isinstance(player.race, (str))
    assert isinstance(player.religion, (str))
    assert isinstance(player.language, (str))
    assert isinstance(player.name, (str))
    assert isinstance(player.level, (int))


def test_load_dimensions_append():
    player = mc.Player()
    player.load_dimensions(how='append', player_class=['wizard', 'general', 'edain'])

    assert len(player.player_class_options) == 7

def test_load_dimensions_overwrite():
    player = mc.Player()
    player.load_dimensions(how='overwrite', player_class=['wizard', 'general', 'edain'])

    assert len(player.player_class_options) == 3

def test_mod():
    # placeholder for tests of the mod() method
    pass