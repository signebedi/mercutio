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

player.default # generates an empty character sheet, an alias for mercutio.gen() without passing args
player.graphical # starts the graphical, CLI character creation interface
player.random # generates a random character sheet

# you can also pass the values for each dimension you'd like to pass to the gen() method, which will
# leave dimensions as empty strings when not passed

player.gen(
  player_class='warrior',
  # attributes={
  #   'str': 5,
  #   'con': 3,
  #   'int': 2,
  #   'wis': 3,
  #   'dex': 2,
  #   'agi': 3,
  # },
  name='balthor batwing, earl of pentham',
)

# you can also load your own dimensions in a python dictionary, using two methods

# method one: overwrite default dimensions

dimensions = mc.load(data = DICT, how='overwrite') # overwriting
player.gen(dimensions=dimensions).default

# method two: append to default dimensions

dimensions = mc.load(data = DICT, how='append') # appending
player.gen(dimensions=dimensions).default

# you can write your character details to a pickle file using the save() method

player.save()

# you can also load your character details from a pickle file using the load_player() method

player.load_player(filename='balthor batwing, earl of pentham.pickle')


```
## next steps
* **DONE** build architecture above
* **DONE** replace to_csv/read_csv with pickle
* fix player attributes -- it's broken right now, doesn't allow the user to pass values for each of their attributes
* add pytest unit tests
* finish configuring support for travis ci

---
Copyright (c) 2020 Signe Janoska-Bedi
