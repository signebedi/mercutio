# Getting Started 
---

![dragon gif](cropped.gif)

yet another character creation engine

See our GitHub repo at [github.com/signebedi/mercutio](https://github.com/signebedi/mercutio).

## Overview

Mercutio provides a straightforward, stable, and highly-customizable API for character creation. It provides default and optional character dimensions, along with vanilla options for each dimension:

* **class**: [default] warrior, mage, rogue, ranger
* **attributes**: [default] strength, constitution, intelligence, wisdom, dexterity, charisma
* **race**: [optional] human, elf, dwarf, orc, halfling
* **religion**: [optional] none, branchala, habbakuk, kiri-jolith, majere, mishakal, paladine, solinari, chislev, gilean, lunitari, reorx, shinare, sirrion, zivilyn, chemosh, hiddukel, morgion, nuitari, sargonnas, takhisis, zeboim
* **language**: [optional] common, dwarvish, elvish, giant, gnomish, goblin, halfling, orc
* **special**: [optional] 
* **skills**: [optional]
* **equipment**: [optional]
* **spells**: [optional]
* **attacks**: [optional]
* **alignment**: [optional] {'personal: [chaotic, neutral, lawful], 'moral': [good, evil, neutral]}

In addition, it tracks vital data such as level, experience, alignment, and hit-points.

## Usage

Start by importing the mercutio library:
```python
import mercutio.mercutio as mc
```

Next, you can create your player object:

```python
player = mc.Player()
```

You can also pass the values for each dimension you'd like to pass to the gen() method. Note: this method will leave dimensions empty when they are not passed:
```python
player.gen(
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
  religion='paladine',
  race='human',
  language='common'
)
```

You can also use the graphical player creation interface:
```python
player.gen(graphical=True) # starts the graphical, CLI character creation interface
```


You can also generate entirely random players:
```python
player.gen(random=True, ...) # generates a random character sheet
```
Or you can randomize individual characteristics by passing the 'RANDOM' keyword to Player.gen():
```python
player.gen(
  player_class='RANDOM',
)
```

Modify an existing player using the mod() method:

```python
player.mod(name='beringor barthenon, guardian of bradley gardens')
```

Write your character details to a pickle file using the save() method. Note, this will save your character under their designated name and may experience errors if you used non-friendly characters:
```python
player.save()
```

Load character details from a pickle file using the load_player() method:
```python
player.load_player(filename='balthor batwing, earl of pentham.pickle')
```

Load your custom dimensions from python lists, using two methods:

Method one: overwrite default dimensions
```python
import mercutio.mercutio as mc
player = mc.Player()
player.load_dimensions(how='overwrite', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```

Method two: append to default dimensions
```python
import mercutio.mercutio as mc
player = mc.Player()
player.load_dimensions(how='append', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```