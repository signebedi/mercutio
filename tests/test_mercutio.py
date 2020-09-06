import pytest
import mercutio as mc

def test_gen():
    player = mc.Player()
    player.gen()

    assert isinstance(player.player_class, (str))
    assert isinstance(player.race, (str))
    assert isinstance(player.religion, (str))
    assert isinstance(player.language, (str))
    assert isinstance(player.name, (str))
    assert isinstance(player.level, (int))
    assert isinstance(player.attributes, (dict))
    assert isinstance(player.skills, (dict))

# test that overwriting player dimensions works as expected 
def test_load_dimensions_append():
    player = mc.Player()
    player.load_dimensions(how='append', player_class=['wizard', 'general', 'edain'])

    assert len(player.player_class_options) == 7

# test that overwriting player dimensions works as expected 
def test_load_dimensions_overwrite():
    player = mc.Player()
    player.load_dimensions(how='overwrite', player_class=['wizard', 'general', 'edain'])

    assert len(player.player_class_options) == 3

# test that modifications to player stats work as expected
def test_mod():
    player = mc.Player()
    player.gen(name='balthor batwing, earl of pentham',)

    player.mod(name='beringor barthenon, guardian of bradley gardens')

    assert player.name == 'beringor barthenon, guardian of bradley gardens'

# test that dice-rolls return values w/i expected ranges
def test_dice():
    roll = mc.Roll() # instantiate the Roll() class

    assert all([roll.four() for _ in range(100)]) in range(1,5) 
    assert all([roll.eight() for _ in range(100)]) in range(1,9) 
    assert all([roll.ten() for _ in range(100)]) in range(1,11) 
    assert all([roll.twelve() for _ in range(100)]) in range(1,13) 
    assert all([roll.twenty() for _ in range(100)]) in range(1,21) 
