# mercutio

yet another character creation engine

[![Build Status](https://travis-ci.org/signebedi/mercutio.svg?branch=master)](https://travis-ci.org/signebedi/mercutio)


## overview

mercutio provides a straightforward API for creating RPG characters. By default, if provides two default and four optional character dimensions, along with vanilla options for each dimension:

* **class**: [default] warrior, mage, rogue, ranger
* **attributes**: [default] strength, constitution, intelligence, wisdom, dexterity, agility
* **race**: [optional] human, elf, dwarf, orc, halfling
* **religion**: [optional] 
* **language**: [optional]
* **special**: [optional] 

```python
from mercutio import Mercutio as mc

player = mc()

# you can also pass the values for each dimension you'd like to pass to the gen() method, 
# which will leave dimensions as empty strings when not passed

player.gen(
  player_class='warrior',
  attributes={
    'strength': 5,
    'constitution': 3,
    'intelligence': 2,
    'wisdom': 3,
    'dexterity': 2,
    'agility': 3,
  },
  name='balthor batwing, earl of pentham',
)

# you can write your character details to a pickle file using the save() method

player.save()

# you can also load your character details from a pickle file using the load_player() method

player.load_player(filename='balthor batwing, earl of pentham.pickle')
```

## next steps
* **DONE 8.25.20** build architecture above
* **DONE 8.25.20** replace to_csv/read_csv with pickle
* **DONE 8.25.20** doesn't allow the user to pass values for each of their attributes
* **DONE 8.25.20, but needs more** add pytest unit tests
* **DONE 8.25.20** finish configuring support for travis ci
* add the following methods
```python
player.default # generates empty character, alias for mercutio.gen() without args
player.graphical # starts the graphical, CLI character creation interface
player.random # generates a random character sheet


# you can also load custom dimensions from a python dictionary, using two methods

# method one: overwrite default dimensions
dimensions = mc.load_dimensions(how='overwrite', ...) # overwriting
player.gen(dimensions=dimensions).default

# method two: append to default dimensions
dimensions = mc.load_dimensions(how='append', ...) # appending
player.gen(dimensions=dimensions).default
```

---
Copyright (c) 2020 Signe Janoska-Bedi
