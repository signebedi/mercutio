# Getting Started 
---

![dragon gif](cropped.gif)

yet another character creation engine

See our GitHub repo at [github.com/signebedi/mercutio](https://github.com/signebedi/mercutio).

## Overview

Mercutio provides a straightforward, stable, and highly-customizable API for character creation. It provides default and optional player dimensions, along with vanilla options for each dimension:

* **class**: [default] warrior, mage, rogue, ranger
* **attributes**: [default] strength, constitution, intelligence, wisdom, dexterity, charisma
* **race**: [optional] human, elf, dwarf, orc, halfling
* **religion**: [optional] none, branchala, habbakuk, kiri-jolith, majere, mishakal, paladine, solinari, chislev, gilean, lunitari, reorx, shinare, sirrion, zivilyn, chemosh, hiddukel, morgion, nuitari, sargonnas, takhisis, zeboim
* **language**: [optional] common, dwarvish, elvish, giant, gnomish, goblin, halfling, orc
* **skills**: [optional] athletics, acrobatics, sleight, stealth, arcana, history, investigation, nature, religion, animal-handling, insight, medicine, perception, survival, deception, intimidation, performance, persuasion

In the future, support may be added for the following dimensions:
* **equipment**: [optional]
* **spells**: [optional]
* **attacks**: [optional]
* **alignment**: [optional] {'personal: [chaotic, neutral, lawful], 'moral': [good, evil, neutral]}

In addition, support may be added for vital data such as experience, alignment, and hit-points.

## Usage

Start by importing the mercutio library:
```python
import mercutio as mc
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
    'strength': 7,
    'constitution': 5,
    'intelligence': 4,
    'wisdom': 3,
    'dexterity': 4,
    'charisma': 6,
  },
  name='balthor batwing, earl of pentham',
  religion='paladine',
  race='human',
  language='common'
  level=3 # defaults to level 1
  skills={
    'athletics': 8,
    'acrobatics': 6,
    'sleight': 3,
    'stealth': 1,
    'arcana': 2,
    'history': 1,
    'investigation': 2,
    'nature': 2,
    'religion': 4,
    'animal-handling': 2,
    'insight': 3,
    'medicine': 1,
    'perception': 4,
    'survival': 3,
    'deception': 4,
    'intimidation': 5,
    'performance': 5,
    'persuasion': 7,
  },
)
```
Note: it is highly recommended that you do not pass base values for player attributes or skills, since the engine will randomize these between 1 and 10 when no arguments are passed. However, this argument remains in case you are interested in, for example, replicating an existing player.

You can also use the graphical player creation interface:
```python
player.gen(graphical=True) # starts the graphical, CLI character creation interface
```


You can also generate entirely random players:
```python
player.gen(random=True, ...) # generates a random character sheet
```
Or you can randomize individual dimensions in most cases by simply not passing a value for them. Dimensions that are not passed by the user will generally be randomized by default, which has thus far proven to be the most stable approach to this issue (Exceptions: name[defaults to empty string], language[defaults to 'common']), religion[defaults to 'none'], skills [defaults to empty string]):

Modify an existing player using the mod() method:
```python
player.mod(name='beringor barthenon, guardian of bradley gardens')
```

Write your character details to a pickle file using the save() method. Note, this will save your character under their designated name and may experience errors if you used certain characters based on your system requirements:
```python
player.save()
```
You can use a custome name using ```player.save(filename='player_one')``` but be careful not to add the file extension, since mercutio does that for you.

You can also write to a more user-friendly CSV format -- note the program uses pipe | delimiters to allow for flexibility in characters used in player dimensions:
```python
player.save(csv=True)
```

Load character details from a pickle file using the load_player() method -- noted that CSV files cannot be loaded at this time:
```python
player.load_player(filename='balthor batwing, earl of pentham.pickle')
```

Load your custom dimensions from python lists, using two methods:

Method one: overwrite default dimensions
```python
import mercutio as mc
player = mc.Player()
player.load_dimensions(how='overwrite', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```

Method two: append to default dimensions
```python
import mercutio as mc
player = mc.Player()
player.load_dimensions(how='append', player_class=['wizard', 'general', 'edain'])
player.gen(player_class='wizard', ...)
```

Another key element of loading dimensions is also passing additional buffs, which are stored in ```mercutio.defaults``` as buff_options list, and each individual buff follows the following structure:

```python
{
  'name':'wizard', #  designate the player identifier that will trigger this buff
  'dimension': 'class', # designates which dimension the 'name' option falls under
  'buff': {'strength':-1,'intelligence':3,}, #  designates the character skills or attributes to buff
}
```

In order for the new character dimensions you pass to have any impact of character atttributes and skills, you need to pass details about the the impact these have:
```python
PLACEHOLDER FOR API FOR MODIFYING BUFFS -- only provide an append option
```

The program also provides an API for rolling dice using the ```mc.Roll()``` class:

```python
roll = mc.Roll() # instantiate the Roll() class

# now you can call dice rolls 
roll.four() 
roll.six()
roll.eight()
roll.ten()
roll.twelve()
roll.twenty()

```
