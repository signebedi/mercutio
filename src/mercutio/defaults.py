"""defaults.py: sets default player options mercutio, a straightforward, stable, and highly-customizable API for character creation"""


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
  {  
    'name':'wizard', 
    'dimension': 'class',  
    'proficiencies': {'staffs':1, 'crossbows':1, 'slings':1,},  
    'random':{'number':2, 'choice':['arcana', 'history', 'insight', 'investigation', 'medicine', 'religion']}, 
  },
  {  
    'name':'fighter', 
    'dimension': 'class',  
    'proficiencies': {'leather':1, 'hide':1, 'chain':1, 'scale':1, 'breastplate':1, 'halfplate':1, 'ringmail':1, 'chainmail':1, 'splint':1, 'plate':1, 'axes':1, 'bows':1, 'brawling':1, 'staffs':1, 'crossbows':1, 'flails':1, 'maces':1, 'blades':1, 'polearms':1, 'shields':1, 'spears':1, 'slings':1, }, 
    'random': {'number':2, 'choice':['acrobatics', 'animal-handling', 'athletics', 'history', 'insight', 'intimidation', 'perception', 'survival']}, 
  },
  {  
    'name':'rogue', 
    'dimension': 'class',  
    'proficiencies': {'axes':1, 'brawling':1, 'staffs':1, 'flails':1, 'maces':1, 'spears':1, 'slings':1, 'leather':1, 'hide':1, 'chain':1, },   
    'random':{'number':4, 'choice':['acrobatics', 'athletics', 'deception', 'insight', 'intimidation', 'investigation', 'perception', 'performance', 'persuasion', 'sleight', 'stealth']}, 
  },
  {
    'name':'cleric', 
    'dimension': 'class',  
    'proficiencies': {'leather':1, 'hide':1, 'chain':1, 'scale':1, 'breastplate':1, 'axes':1, 'brawling':1, 'staffs':1, 'flails':1, 'maces':1, 'shields':1, 'spears':1, 'slings':1,}, 
    'random':{'number':2, 'choice':['history', 'insight', 'medicine', 'persuasion', 'religion']}, 
  },
  {  'name':'human', 'dimension': 'race',  'proficiencies': {'strength':1,'dexterity':1,'constitution':1,'intelligence':1,'wisdom':1,'charisma':1,},  },
  {  'name':'elf', 'dimension': 'race',  'proficiencies': {'dexterity':2,},  },
  {  'name':'wood elf', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'wisdom':1, 'bows':1, 'blades':1,},  },
  {  'name':'high elf', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'intelligence':1, 'bows':1, 'blades':1,},  },
  {  'name':'dark elf', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'charisma':1, 'bows':1, 'blades':1,},  },
  {  'name':'dwarf', 'dimension': 'race',  'proficiencies': {'constitution':2,},  },
  {  'name':'hill dwarf', 'dimension': 'race',  'proficiencies': {'constitution':2, 'wisdom':1,'leather':1, 'hide':1, 'chain':1, 'scale':1, 'breastplate':1, },  },
  {  'name':'mountain dwarf', 'dimension': 'race',  'proficiencies': {'constitution':2, 'strength':2,},  },
  {  'name':'halfling', 'dimension': 'race',  'proficiencies': {'dexterity':2,},  },
  {  'name':'stout halfling', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'constitution':1,},  },
  {  'name':'lightfoot halfling', 'dimension': 'race',  'proficiencies': {'dexterity':2, 'charisma':1,},  },
  {  'name': 'acolyte', 'dimension': 'background',  'proficiencies': {'insight':1, 'religion':1},  },
  {  'name': 'criminal', 'dimension': 'background',  'proficiencies': {'deception':1, 'stealth':1},  },
  {  'name': 'folk hero', 'dimension': 'background',  'proficiencies': {'animal-handling':1, 'survival':1},  },
  {  'name': 'noble', 'dimension': 'background',  'proficiencies': {'history':1, 'persuasion':1},  },
  {  'name': 'sage', 'dimension': 'background',  'proficiencies': {'arcana':1, 'history':1},},
  {  'name': 'soldier', 'dimension': 'background',  'proficiencies': {'athletics':1, 'intimidation':1},  },
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
    {'name': 'axes', 'dimension': 'weapon'},
    {'name': 'bows', 'dimension': 'weapon'},
    {'name': 'brawling', 'dimension': 'weapon'},
    {'name': 'staffs', 'dimension': 'weapon'},
    {'name': 'crossbows', 'dimension': 'weapon'},
    {'name': 'flails', 'dimension': 'weapon'},
    {'name': 'maces', 'dimension': 'weapon'},
    {'name': 'blades', 'dimension': 'weapon'},
    {'name': 'polearms', 'dimension': 'weapon'},
    {'name': 'shields', 'dimension': 'weapon'},
    {'name': 'spears', 'dimension': 'weapon'},
    {'name': 'slings', 'dimension': 'weapon'},
    {'name': 'leather', 'dimension': 'armor'},
    {'name': 'hide', 'dimension': 'armor'},
    {'name': 'chain', 'dimension': 'armor'},
    {'name': 'scale', 'dimension': 'armor'},
    {'name': 'breastplate', 'dimension': 'armor'},
    {'name': 'halfplate', 'dimension': 'armor'},
    {'name': 'ringmail', 'dimension': 'armor'},
    {'name': 'chainmail', 'dimension': 'armor'},
    {'name': 'splint', 'dimension': 'armor'},
    {'name': 'plate', 'dimension': 'armor'},

]

# 'random':['number':4, 'choice':{['acrobatics', 'athletics', 'deception', 'insight', 'intimidation', 'investigation', 'perception', 'performance', 'persuasion', 'sleight', 'stealth']}]
# 'random':[{'number':2, 'choice':['arcana', 'history', 'insight', 'investigation', 'medicine', 'religion']}]
