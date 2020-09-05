# Checklist

## Finished
* **DONE 8.25.20** build architecture above
* **DONE 8.25.20** replace to_csv/read_csv with pickle
* **DONE 8.25.20** doesn't allow the user to pass values for each of their attributes
* **DONE 8.25.20, but needs more!** add pytest unit tests
* **DONE 8.25.20** finish configuring support for travis ci
* **DONE 8.26.20** add docs and transfer this readme
* **DONE 8.26.20** add the ability to modify a player object
* **DONE 8.29.20** add graphical character creation method
```python
player.gen(graphical=True) # starts the graphical, CLI character creation interface
```
* **DONE 9.4.20** add support for language
* **DONE 9.4.20** add support for religion
* **DONE 9.4.20** add support for writing to csv
* **DONE 9.4.20** add random character creation method
```python
player.gen(random=True, ...) # generates a random character sheet
```
* **DONE 9.4.20** add support for dice rolls/random attributes
* **DONE 9.4.20 -- changed mercutio.py to __init__.py** simplify import process -- right now, you import the library using ```import mercutio.mercutio as mc``` but this should just be ```import mercutio as mc``` 
* **DONE 9.4.20** add support for saving to custom filenames
* **DONE 9.5.20**  add badges for stable release version and/or PYPI release, licence  and dependency status
* **DONE 9.5.20** Upload to PYPI https://packaging.python.org/tutorials/packaging-projects/
* * upload using Twine https://twine.readthedocs.io/en/latest/

## In Progress
* build more tests!!

## Future Projects
* **BEFORE v1.0.0**add support for special buffs that can mapped to specific classes/races/religions/languages (eg. a separate dictionary) -- in fact, you could even just replace the current structure with a single data structure that allows the user to specify >> this will make the API more forgiving; underlying question: should attributes then be handled separately to avoid potential concurrency/ordering problems?
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
* **BY v1.0.0**add python-semantic-release to automate [sematic versioning](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/index.html#automatic) with travis-ci and setuptools 
* **BY v1.0.0** add a changelog and autogenerate portions based on git commits -- this means you need to start being more careful about commit messages, especially after the 1.0.0 release 
* * https://keepachangelog.com/en/1.0.0/
* * https://stackoverflow.com/questions/3523534/good-ways-to-manage-a-changelog-using-git
* * https://www.freecodecamp.org/news/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/
* * https://medium.com/better-programming/create-your-own-changelog-generator-with-git-aefda291ea93
* **BY v1.0.0** conduct a thorough review of tests/test_mercutio.py and revise/build upon these as appropriate for future anticipated builds
* **BY v2.0.0** add support for exp, hp, spells, attacks, and equipment
