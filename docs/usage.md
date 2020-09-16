# Usage
---

## Creating Players

Start by installing mercutio over pip:
```
pip install mercutio
```

Next, you can import the mercutio library into the development environment of your choice:
```python
import mercutio as mc
```

Next, you can create your player object:

```python
player = mc.Player()
```

You can also pass the values for each dimension you'd like to pass to the gen() method. Note: this method will generally randomize player dimensions when they are not passed:
```python
player.gen(
  name='balthor batwing, earl of pentham',
  player_class='fighter'
  background='soldier',
  religion='paladine',
  race='human',
  language='common',
  skills={'athletics':1, 'intimidation':1, 'survival':1, 'insight':1},
)
```
Note: it is highly recommended that you do not pass base values for proficiencies -- especially attribute, weapon, armor, and tool proficiencies, since the engine will randomize these when no arguments are passed. However, this argument remains in case you are interested in, for example, replicating an existing player.

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

## Saving Players

Write your character details to a pickle file using the save() method. Note, this will save your character under their designated name and may experience errors if you used certain characters based on your system requirements:
```python
player.save()
```
You can use a custome name using ```player.save(filename='player_one')``` but be careful not to add the file extension, since mercutio does that for you.

You can also write to a more user-friendly CSV format -- note the program uses pipe | delimiters to allow for flexibility in characters used in player dimensions:
```python
player.save(csv=True)
```

Load character details from a pickle file using the load() method -- noted that CSV files cannot be loaded at this time:
```python
player.load(filename='balthor batwing, earl of pentham.pickle')
```

## Customization

Load custom dimensions by adding new character dimensions for buffs:
```python
buffs = [
  {
    'name':'necromancer', 
    'dimension': 'class', 
    'proficiencies': {'strength':-1,'intelligence':3,},
  },
  {
    'name':'general',
    'dimension': 'class',
    'proficiencies': {'strength':3,'intelligence':1,'wisdom':1,}, 
  },
  {
    'name':'edain',
    'dimension': 'class', 
    'proficiencies': {'strength':2,'dexterity':2,'constitution':1}
  },
]
```

... and proficiencies:
```python
proficiencies = [
    {
        'name': 'will',
        'dimension': 'attribute',
    },
    {
        'name': 'greed',
        'dimension': 'attribute',
    },
    {
        'name': 'pride',
        'dimension': 'attribute',
    },
]
```

Finally, load your custom dimensions using two methods:

Method one: overwrite default dimensions
```python
player.customize(how='overwrite', buffs=buffs, proficiencies=proficiencies)
player.gen(player_class='necromancer', ...)
```

Method two: append to default dimensions
```python
player.customize(how='append', buffs=buffs, proficiencies=proficiencies)
player.gen(player_class='necromancer', ...)
```

As a note, loading dimensions will typically be significantly less buggy when run **prior** to using ```mc.Player().gen()```.

## Dice Rolls

Mercution also provides an API for rolling dice using the ```mc.Roll()``` class:

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