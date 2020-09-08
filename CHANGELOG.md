# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Changes will fall under the following categories:
- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

## [Unreleased]
### Added
- support for exp, hp, size, speed, spells, attacks, and equipment (default to starting equipment, but allow add'l items to be added) customization
- python-semantic-release to automate [sematic versioning](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/index.html#automatic) with travis-ci, twine, github tags/releases, and setuptools
- support for multiclassing and multiple languages
- support for proficiencies, ability checks and saving throws instead of skill values
- leveling bonuses for skills and attributes


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


[Unreleased]: https://github.com/signebedi/mercutio/compare/0.7.1...HEAD
[0.7.1]: https://github.com/signebedi/mercutio/compare/0.7.0...0.7.1
[0.7.0]: https://github.com/signebedi/mercutio/compare/0.6.0...0.7.0
[0.6.0]: https://github.com/signebedi/mercutio/compare/0.5.1...0.6.0
[0.5.1]: https://github.com/signebedi/mercutio/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/signebedi/mercutio/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/signebedi/mercutio/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/signebedi/mercutio/compare/v.0.2-beta...0.3.0
[0.2.0]: https://github.com/signebedi/mercutio/releases/tag/v.0.2-beta
