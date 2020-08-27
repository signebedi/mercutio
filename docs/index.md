# Mercutio 

yet another character creation engine
---
See our GitHub repo at [github.com/signebedi/mercutio](https://github.com/signebedi/mercutio).

![dragon gif](cropped.gif)

## Getting Started

Mercutio provides a straightforward API for character creation. It provides default and optional character dimensions, along with vanilla options for each dimension:

* **class**: [default] warrior, mage, rogue, ranger
* **attributes**: [default] strength, constitution, intelligence, wisdom, dexterity, charisma
* **race**: [optional] human, elf, dwarf, orc, halfling
* **religion**: [optional] 
* **language**: [optional]
* **special**: [optional] 
* **skills**: [optional]
* **alignment**: [optional] {'personal: [chaotic, neutral, lawful], 'moral': [good, evil, neutral]}

## Usage

Start by importing the mercutio library
```python
import mercutio.mercutio as mc
```

Next, you can create your player object

```python
player = mc.Mercutio()
```

You can also pass the values for each dimension you'd like to pass to the gen() method. Note: this method will leave dimensions empty when they are not passed.
```python
player.gen()
  player_class='warrior',
  attributes={
    'strength': 5,
    'constitution': 3,
    'intelligence': 2,
    'wisdom': 3,
    'dexterity': 2,
    'charisma': 3,
  },
  name='balthor batwing, earl of pentham',
)
```
Modify an existing player using the mod() method:

```python
player.mod(name='beringor barthenon, guardian of bradley gardens')
```

Write your character details to a pickle file using the save() method. Note, this will save your character under their designated name and may experience errors if you used non-friendly characters.

```python
player.save()
```
Load character details from a pickle file using the load_player() method.

```python
player.load_player(filename='balthor batwing, earl of pentham.pickle')
```

Load your custom dimensions from python lists, using two methods:

Method one: overwrite default dimensions
```python
import mercutio.mercutio as mc
player = mc.Mercutio()
player.load_dimensions(how='overwrite', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```

Method two: append to default dimensions
```python
import mercutio.mercutio as mc
player = mc.Mercutio()
player.load_dimensions(how='append', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```

## Checklist

* **DONE 8.25.20** build architecture above
* **DONE 8.25.20** replace to_csv/read_csv with pickle
* **DONE 8.25.20** doesn't allow the user to pass values for each of their attributes
* **DONE 8.25.20, but needs more!** add pytest unit tests
* **DONE 8.25.20** finish configuring support for travis ci
* **DONE 8.26.20** add docs and transfer this readme
* **DONE 8.26.20** add the ability to modify a player object
* add graphical and random character creation methods
```python
player.graphical # starts the graphical, CLI character creation interface
player.random # generates a random character sheet
```
* add support for exp, hp, spells, attacks, and equipment
* add support for dice rolls/random attributes
* add support for special buffs that can mapped to specific classes/races/religions/languages (eg. a separate dictionary) -- in fact, you could even just replace the current structure with a single data structure that allows the user to specify >> this will make the API more forgiving
```python
default_options = [
  {
    'name':'strength',
    'dimension': 'attribute',
    'value':0, # default value
  },
  {
    'name':'mage',
    'dimension': 'class',
    'buff':{'intelligence':3,'wisdom':1,'strength':-1},
  },
  {
    'name':'',
    'dimension': '',
    'value': 0,
    'buff':{},
  },
]
```
