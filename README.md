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
* **specials**: [optional] 

```python
from mercutio import mercutio

player = mercutio.gen().default # generates an empty character sheet, an alias for mercutio.gen() without passing args
player = mercutio.gen().graphical # starts the graphical, CLI character creation interface
player = mercutio.gen().random # generates a random character sheet

# you can also pass the values for each dimension you'd like to pass to the gen() method, which will
# leave dimensions as empty strings when not passed

player = mercutio.gen(
  class='warrior',
  attributes={
    'str': 5,
    'con': 3,
    'int': 2,
    'wis': 3,
    'dex': 2,
    'agi': 3,
  },
  'name': 'balthor batwing, earl of pentham',
)

# you can also load your own dimensions in a python dictionary, using two methods

# method one: overwrite default dimensions

dimensions = mercutio.load(data = DICT, how='overwrite') # overwriting
player.gen(dimensions=dimensions).default

# method two: append to default dimensions

dimensions = mercutio.load(data = DICT, how='append') # appending
player.gen(dimensions=dimensions).default

# finally, you can write your character details to a CSV file using the to_csv() method

player.to_csv(filename='player.csv')
```
Copyright (c) 2020 Signe Janoska-Bedi
