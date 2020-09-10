# religion src: https://1d4chan.org/wiki/Gods_of_Dungeons_and_Dragons#Dragonlance

# Gods of Good
# Branchala (the harp), music, inspiration, bards
# Habbakuk (the phoenix), persistence, animals, rangers
# Kiri-Jolith (the bison's head), unity, strength, fighters
# Majere (the rose), discipline, dreams, monks
# Mishakal (the figure-eight), restoration, motherhood, healers
# Paladine (the platinum dragon), majesty, aspirations, leaders
# Solinari (the silver moon), magic used for good, wizards
# Gods of Neutrality
# Chislev (a wandering star (planet)), instinct, natural world
# Gilean (the book), knowledge, librarians, scholars
# Lunitari (the red moon), magic used for neutrality, wizards
# Reorx (a red star), creation, craftsmen, dwarves and gnomes
# Shinare (a wandering star (planet)), interaction, agreements, merchants
# Sirrion (a wandering star (planet)), transformation, fire, artists and alchemists
# Zivilyn (a wandering star (planet)), wisdom, awareness, completely impartial
# Gods of Evil
# Chemosh (the goat skull), fatalism, despair, undead
# Hiddukel (the broken scale), exploitation, selfishness, thieves
# Morgion (the diseased hood), decay, disease, suffering
# Nuitari (the black (invisible) moon), magic used for evil, wizards
# Sargonnas (the condor), wrath, revenge, minotaurs
# Takhisis (the five-headed dragon), control, conquest, tyrants
# Zeboim (the dragon-turtle), strife, mood-swings, bane of sailors


buffs = [
  {  'name':'wizard', 'dimension': 'class',  'proficiencies': {},  },
  {  'name':'fighter', 'dimension': 'class',  'proficiencies': {},  },
  {  'name':'rogue', 'dimension': 'class',  'proficiencies': {},   },
  {  'name':'cleric', 'dimension': 'class',  'proficiencies': {},  },
  {  'name':'human', 'dimension': 'race',  'proficiencies': {'strength':1,'dexterity':1,'constitution':1,'intelligence':1,'wisdom':1,'charisma':1,},  },
  {  'name':'elf', 'dimension': 'race',  'proficiencies': {'dexterity':2,},  },
  {  'name':'wood elf', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'wisdom':1,},  },
  {  'name':'high elf', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'intelligence':1,},  },
  {  'name':'dark elf', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'charisma':1,},  },
  {  'name':'dwarf', 'dimension': 'race',  'proficiencies': {'constitution':2,},  },
  {  'name':'hill dwarf', 'dimension': 'race',  'proficiencies': {'constitution':2, 'wisdom':1,},  },
  {  'name':'mountain dwarf', 'dimension': 'race',  'proficiencies': {'constitution':2, 'strength':2,},  },
  {  'name':'halfling', 'dimension': 'race',  'proficiencies': {'dexterity':2,},  },
  {  'name':'stout halfling', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'constitution':1,},  },
  {  'name':'lightfoot halfling', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'charisma':1,},  },
  {  'name': 'acolyte', 'dimension': 'background',  'proficiencies': {},  },
  {  'name': 'criminal', 'dimension': 'background',  'proficiencies': {},  },
  {  'name': 'folk hero', 'dimension': 'background',  'proficiencies': {},  },
  {  'name': 'noble', 'dimension': 'background',  'proficiencies': {},  },
  {  'name': 'sage', 'dimension': 'background',  'proficiencies': {'arcana':1, 'history':1},},
  {  'name': 'soldier', 'dimension': 'background',  'proficiencies': {'strength':1,},  },
  {  'name':'common', 'dimension':'language','proficiencies':{}   },
  {  'name':'dwarvish', 'dimension':'language','proficiencies':{}   },
  {  'name':'elvish', 'dimension':'language','proficiencies':{}   },
  {  'name':'giant', 'dimension':'language','proficiencies':{}   },
  {  'name':'gnomish', 'dimension':'language','proficiencies':{}   },
  {  'name':'goblin', 'dimension':'language','proficiencies':{}   },
  {  'name':'halfling', 'dimension':'language','proficiencies':{}   },
  {  'name':'orc', 'dimension':'language','proficiencies':{}   },
  {  'name':'none', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'branchala', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'habbakuk', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'kiri-jolith', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'majere', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'mishakal', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'paladine', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'solinari', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'chislev', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'gilean', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'lunitari', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'reorx', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'shinare', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'sirrion', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'zivilyn', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'chemosh', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'hiddukel', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'morgion', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'nuitari', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'sargonnas', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'takhisis', 'dimension':'religion', 'proficiencies': {}   },
  {  'name':'zeboim', 'dimension':'religion', 'proficiencies': {}   },

]

### still need to add weapon, armor, tool proficiencies
proficiencies = [
    {'name': 'athletics', 'dimension': 'skill'},
    {'name': 'acrobatics', 'dimension': 'skill'},
    {'name': 'sleight', 'dimension': 'skill'},
    {'name': 'stealth', 'dimension': 'skill'},
    {'name': 'arcana', 'dimension': 'skill'},
    {'name': 'history', 'dimension': 'skill'},
    {'name': 'investigation', 'dimension': 'skill'},
    {'name': 'nature', 'dimension': 'skill'},
    {'name': 'religion', 'dimension': 'skill'},
    {'name': 'animal-handling', 'dimension': 'skill'},
    {'name': 'insight', 'dimension': 'skill'},
    {'name': 'medicine', 'dimension': 'skill'},
    {'name': 'perception', 'dimension': 'skill'},
    {'name': 'survival', 'dimension': 'skill'},
    {'name': 'deception', 'dimension': 'skill'},
    {'name': 'intimidation', 'dimension': 'skill'},
    {'name': 'performance', 'dimension': 'skill'},
    {'name': 'persuasion', 'dimension': 'skill'},
    {'name': 'strength', 'dimension': 'attribute'},
    {'name': 'constitution', 'dimension': 'attribute'},
    {'name': 'intelligence', 'dimension': 'attribute'},
    {'name': 'wisdom', 'dimension': 'attribute'},
    {'name': 'dexterity', 'dimension': 'attribute'},
    {'name': 'charisma', 'dimension': 'attribute'},
]