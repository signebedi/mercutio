import pytest
import mercutio.mercutio as mc

def test_gen():
    player = mc.Mercutio()
    player.gen()

    assert isinstance(player.player_class, (str))
    assert isinstance(player.race, (str))
    assert isinstance(player.religion, (str))
    assert isinstance(player.language, (str))
    assert isinstance(player.name, (str))
    assert isinstance(player.level, (int))


