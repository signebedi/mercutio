# mercutio

yet another character creation engine

[![Build Status](https://travis-ci.org/signebedi/mercutio.svg?branch=master)](https://travis-ci.org/signebedi/mercutio)


## overview

mercutio provides a straightforward API for creating RPG characters. By default, if provides two default and four optional character dimensions, along with vanilla options for each dimension:

* **class**: [default] warrior, mage, rogue, ranger
* **attributes**: [default] strength, constitution, intelligence, wisdom, dexterity, charisma
* **race**: [optional] human, elf, dwarf, orc, halfling
* **religion**: [optional] 
* **language**: [optional]
* **special**: [optional] 

```python
import mercutio.mercutio as mc

player = mc.Mercutio()

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

# you can also load custom dimensions from python lists, using two methods

# method one: overwrite default dimensions
import mercutio.mercutio as mc
player = mc.Mercutio()
player.load_dimensions(how='overwrite', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)

# method two: append to default dimensions
import mercutio.mercutio as mc
player = mc.Mercutio()
player.load_dimensions(how='append', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```

## next steps
* **DONE 8.25.20** build architecture above
* **DONE 8.25.20** replace to_csv/read_csv with pickle
* **DONE 8.25.20** doesn't allow the user to pass values for each of their attributes
* **DONE 8.25.20, but needs more** add pytest unit tests
* **DONE 8.25.20** finish configuring support for travis ci
* add graphical and random character creation methods
```python
player.graphical # starts the graphical, CLI character creation interface
player.random # generates a random character sheet
```
* add docs and transfer this readme
* add support for special buffs that can mapped to specific classes/races/religions/languages (eg. a separate dictionary) -- in fact, you could even just replace the current structure with a single data structure that allows the user to specify >> this will make the API more forgiving
```python
buff_options = [
  {
    'name':'mage',
    'dimension': 'class',
    'buff':{'intelligence':3,'wisdom':1,'strength':-1},
  },
  {
    'name':'',
    'dimension': '',
    'buff':{},
  },
]

```
---
Copyright (c) 2020 Signe Janoska-Bedi
