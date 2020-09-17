# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Git commits will follow these conventions (with major convetions bolded):

- **Added**: a new feature to the API
- **Removed**: a current feature from the API
- **Changed**: a current feature of the API
- **Fixed**: a broken feature of the API
- **Docs**: modified the API's documentation
- **Tests**: modified the API's tests
- Routine: clerical and minor changes or refactors not affecting the API
- Grumble: progress not yet resulting in any changes above

## [Unreleased]
### Added
- support for exp, hp, size, speed, spells, attacks, if there is demand for this feature
- leveling bonuses for skills and attributes, if there is demand for this feature
- proficiencies for tools, if there is demand for this feature
- support for multiclassing, if there is demand for this feature
- support for multiple languages, if there is demand for this feature

## [0.10.0] - 2020-09-17
### Added
- enable support to add buffs to dice rolls through a wrapper function

## [0.9.4] - 2020-09-17
### Added
- ```Player.distribute()``` method based on the rule that "if a character would gain the same proficiency from two different sources, he or she can choose a different proficiency of the same kind (skill or tool) instead. (PHB, pg. 125)"

### Changed
- Changelog moved to docs/

## [0.9.3] - 2020-09-17
### Added
- proficiency buffs for classes, races and backgrounds

### Fixed
- ```mc.Player.mod()``` problems when name was not set
- tests by moving test_customize_overwrite() to the end because of how it impacts the defaults list

## [0.9.2] - 2020-09-16
### Added
- git commits to release notes

## [0.9.1] - 2020-09-15
### Added
- armor and weapon proficiencies in ```Player.gen()```, ```Player.buff()```, ```Player.mod()```,  and ```Player.load()```
- started following standardized git commit formats

## [0.9.0] - 2020-09-15
### Added
- proficiences for armour, weapons

## [0.8.7] - 2020-09-13
### Fixed
- issues in deployment with header data 

## [0.8.6] - 2020-09-13
### Added
- header data like __author__ and __license__

## [0.8.5] - 2020-09-11
### Fixed
- ```mc.buff()``` so that it only applies buff if the proficiency dict is not empty
- improved tests for ```mc.buff()```

## [0.8.4] - 2020-09-11
### Added
- automated github release 

## [0.8.3] - 2020-09-11
### Added
- __version__ variable 

## [0.8.2] - 2020-09-10
### Fixed
- minor syntax errors in build 

## [0.8.1] - 2020-09-10
### Fixed
- problems with ```Player().customize()``` allowing users to correctly pass new dimensions
- religion so that it is included in buff list
### Changed
- ```load_player()``` is now simply ```load()``` 
- ```load_dimensions()``` is now simply ```customize()```

## [0.8.0] - 2020-09-09
### Added
- proficiencies for skills (armour, weapons, tools to come) measured along the axis of 1 (proficient), 0 (common), and -1 (weak)

### Changed
- skills to simply proficiencies in attributes and skills (armour, weapons, tools to come)

### Removed
- support for option lists in favor of using the buff dictionary for all indexed dimensions/characteristics

## [0.7.2] - 2020-09-09
### Added
- support for proficiencies, ability checks and saving throws instead of skill values

### Changed
- tests for buffs to ensure that proficiencies are well accounted for

## [0.7.1] - 2020-09-07
### Added
- Test for buffs

## [0.7.0] - 2020-09-07
### Added
- support for special buffs that can mapped to specific classes/races/religions/languages
- support for backgrounds
- Documentation for buffs
- Usage docs page

### Changed
- index to [DnD Basic Rules, Version 1.0, Released November 2018](https://media.wizards.com/2018/dnd/downloads/DnD_BasicRules_2018.pdf)

### Removed
- Next Steps docs page, which is now covered by the changelog

## [0.6.0] - 2020-09-06
### Added
- support for dice-rolling using eg. ```mc.Roll().six()```
- tests for dice-rolling

## [0.5.1] - 2020-09-05
### Fixed
- PyPi deployment by adding MANIFEST.in

## [0.5.0] - 2020-09-05
### Added
- first release to PyPi
- requirements for twine

## [0.4.0] - 2020-09-04
### Added
- default options for languages and religion based on standard DnD conventions
- options to save player to CSV file using ```mc.Player.save(csv=True)```
- options to specify the name of the save file using ```mc.Player.save(filename=STRING)```
- random character creation method using ```mc.Player.gen(random=True)```
- changelog based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- dependency testing using requires.io

### Changed
- import method from ```import mercutio.mercutio as mc``` to ```import mercutio as mc```
- ```special``` dimensions are now known as ```skills```, which follow the standard DnD skill list

## [0.3.0] - 2020-08-29
### Added
- graphical character creation method using ```mc.Player.gen(graphical=True)```
- load custom player class, attributes, race, religion, language, and special using ```mc.Player.load_dimensions()```
- started following [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [0.2.0] - 2020-08-26
### Added
- pickle files for saving player details
- load player from pickle files ```mc.Player.load_player()```
- support for readthedocs
- support for Travis-CI
- ability to modify a player object using ```mc.Player.mod()```

## 0.1.0 - 2020-08-25
### Added
- generate player using ```mc.Player.gen()```
- standard player dimensions for class, attributes, race, religion, language, and special

[Unreleased]: https://github.com/signebedi/mercutio/compare/0.10.0...HEAD
[0.10.0]: https://github.com/signebedi/mercutio/compare/0.9.4...0.10.0
[0.9.4]: https://github.com/signebedi/mercutio/compare/0.9.3...0.9.4
[0.9.3]: https://github.com/signebedi/mercutio/compare/0.9.2...0.9.3
[0.9.2]: https://github.com/signebedi/mercutio/compare/0.9.1...0.9.2
[0.9.1]: https://github.com/signebedi/mercutio/compare/0.9.0...0.9.1
[0.9.0]: https://github.com/signebedi/mercutio/compare/0.8.7...0.9.0
[0.8.7]: https://github.com/signebedi/mercutio/compare/0.8.6...0.8.7
[0.8.6]: https://github.com/signebedi/mercutio/compare/0.8.5...0.8.6
[0.8.5]: https://github.com/signebedi/mercutio/compare/0.8.4...0.8.5
[0.8.4]: https://github.com/signebedi/mercutio/compare/0.8.3...0.8.4
[0.8.3]: https://github.com/signebedi/mercutio/compare/0.8.2...0.8.3
[0.8.2]: https://github.com/signebedi/mercutio/compare/0.8.1...0.8.2
[0.8.1]: https://github.com/signebedi/mercutio/compare/0.8.0...0.8.1
[0.8.0]: https://github.com/signebedi/mercutio/compare/0.7.2...0.8.0
[0.7.2]: https://github.com/signebedi/mercutio/compare/0.7.1...0.7.2
[0.7.1]: https://github.com/signebedi/mercutio/compare/0.7.0...0.7.1
[0.7.0]: https://github.com/signebedi/mercutio/compare/0.6.0...0.7.0
[0.6.0]: https://github.com/signebedi/mercutio/compare/0.5.1...0.6.0
[0.5.1]: https://github.com/signebedi/mercutio/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/signebedi/mercutio/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/signebedi/mercutio/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/signebedi/mercutio/compare/v.0.2-beta...0.3.0
[0.2.0]: https://github.com/signebedi/mercutio/releases/tag/v.0.2-beta
