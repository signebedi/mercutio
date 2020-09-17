import pytest

def test_gen():
    import mercutio as mc
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

# test that modifications to player stats work as expected
def test_mod():
    import mercutio as mc
    player = mc.Player()
    player.gen(name='balthor batwing, earl of pentham',)

    player.mod(name='beringor barthenon, guardian of bradley gardens')

    assert player.name == 'beringor barthenon, guardian of bradley gardens'

# test that dice-rolls return values w/i expected ranges when not modified
def test_roll_no_modifier():
    import mercutio as mc
    roll = mc.Roll() # instantiate the Roll() class

    assert all([roll.four() for _ in range(100)]) in range(1,5) 
    assert all([roll.eight() for _ in range(100)]) in range(1,9) 
    assert all([roll.ten() for _ in range(100)]) in range(1,11) 
    assert all([roll.twelve() for _ in range(100)]) in range(1,13) 
    assert all([roll.twenty() for _ in range(100)]) in range(1,21) 

# test that dice-rolls return values w/i expected ranges when modified
def test_roll_with_modifier():
    import mercutio as mc
    roll = mc.Roll() # instantiate the Roll() class

    assert all([roll.four(modifier=10) for _ in range(100)]) in range(1,15) 
    assert all([roll.eight(modifier=10) for _ in range(100)]) in range(1,19) 
    assert all([roll.ten(modifier=10) for _ in range(100)]) in range(1,21) 
    assert all([roll.twelve(modifier=10) for _ in range(100)]) in range(1,23) 
    assert all([roll.twenty(modifier=10) for _ in range(100)]) in range(1,31) 

def test_buffs_not_empty():
    import mercutio as mc
    player = mc.Player()
    player.gen(
        player_class='fighter', 
        name='balthor batwing, earl of pentham', 
        religion='paladine', 
        race='human', 
        language='common',
    )
    attribute_check = player.attributes['strength'] # create a snapshot of the player's attributes

    player.buff(name='human', dimension='race', remove=True) # try removing human buff
    player.buff(name='elf', dimension='race') # then we buff the character

    assert player.attributes['strength'] == attribute_check - 1 # and check that the buff successfully passed


# like the above test, but now we pass purposefully empty buffs to assert this does not break the logic of mc.buff()
def test_buffs_empty():
    import mercutio as mc
    player = mc.Player()

    # append an empty race
    buffs = [
        { 'name':'misanthrope', 'dimension':'race', 'proficiencies': {} },
    ]
    player.customize(how='append', buffs=buffs)

    player.gen(
        player_class='fighter', 
        name='balthor batwing, earl of pentham', 
        religion='paladine', 
        race='human', 
        language='common',
    )
    attribute_check = player.attributes['strength'] # create a snapshot of the player's attributes

    player.buff(name='human', dimension='race', remove=True) # try removing human buff
    player.buff(name=buffs[0]['name'], dimension='race') # then we buff the character with an empty proficiency buff

    assert player.attributes['strength'] == attribute_check - 1 # and check that the LACK of any buff successfully passed

# test the distribute method when we know it will succeed in distributing the additional values
def test_distribute_success():
    import mercutio as mc
    player = mc.Player()

    player.gen(player_class='wizard')
    player.armor['leather']=2
    player.distribute()

    assert player.armor['leather'] == 1

# test the distribute method when we know it will fail in distributing the additional values
def test_distribute_failure():
    import mercutio as mc
    player = mc.Player()

    player.gen(player_class='wizard')
    player.armor['leather']=50
    player.distribute()

    assert player.armor['leather'] != 1


# test that appending to player dimensions works as expected 
def test_customize_append():
    import mercutio as mc
    player = mc.Player()
    class_len = len(player.player_class_options) # create a snapshot of the length of the list of class options

    buffs = [
        { 'name':'wizard', 'dimension':'class'},
        { 'name':'general', 'dimension':'class'},
        { 'name':'edain','dimension':'class'},
    ]

    player.customize(how='append', buffs=buffs)

    assert len(player.player_class_options) == class_len + 3 # assert that this has increased the length of the class list by three

# test that overwriting player dimensions works as expected 
def test_customize_overwrite():
    import mercutio as mc
    player = mc.Player()

    buffs = [
        { 'name':'wizard', 'dimension':'class' },
        { 'name':'general', 'dimension':'class'},
        { 'name':'edain','dimension':'class'   },
    ]

    player.customize(how='overwrite', buffs=buffs)

    assert len(player.player_class_options) == 3
