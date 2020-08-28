# Checklist

* **DONE 8.25.20** build architecture above
* **DONE 8.25.20** replace to_csv/read_csv with pickle
* **DONE 8.25.20** doesn't allow the user to pass values for each of their attributes
* **DONE 8.25.20, but needs more!** add pytest unit tests
* **DONE 8.25.20** finish configuring support for travis ci
* **DONE 8.26.20** add docs and transfer this readme
* **DONE 8.26.20** add the ability to modify a player object
* add graphical and random character creation methods
```python
player.gen(graphical=True) # starts the graphical, CLI character creation interface
player.gen(random=True, ...) # generates a random character sheet
```
* add support for exp, hp, spells, attacks, and equipment
* add support for dice rolls/random attributes
* add support for special buffs that can mapped to specific classes/races/religions/languages (eg. a separate dictionary) -- in fact, you could even just replace the current structure with a single data structure that allows the user to specify >> this will make the API more forgiving; underlying question: should attributes then be handled separately to avoid potential concurrency/ordering problems?
```python
default_dimension_options = [
  {
    'name':'strength',
    'dimension': 'attribute',
    'value':0, # default value
    'buff': {},
  },
  {
    'name':'mage',
    'dimension': 'class',
    'value': None,
    'buff': {'intelligence':3,'wisdom':1,'strength':-1},
  },
  {
    'name':'', # REQUIRED, designate the indentifier for this option
    'dimension': '', # REQUIRED, assign this option to an accepted dimension, see Getting Started above
    'value': None, # OPTIONAL, only if assigning a value to a character skill or attribute
    'buff': {}, # OPTIONAL, only if intended to buff a character skill or attribute
  },
]
```
