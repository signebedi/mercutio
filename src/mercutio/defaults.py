player_class_options = [
    'fighter',    
    'wizard',    
    'rogue',    
    'cleric',    
]

attributes_options = [
    'strength', 
    'constitution', 
    'intelligence', 
    'wisdom', 
    'dexterity', 
    'charisma',
]

race_options = [
    'human', 
    'elf', 
    'wood elf', 
    'high elf', 
    'dark elf', 
    'dwarf', 
    'hill dwarf', 
    'mountain dwarf', 
    'halfling', 
    'stout halfling', 
    'lightfoot halfling', 
]

# src: https://1d4chan.org/wiki/Gods_of_Dungeons_and_Dragons#Dragonlance

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

religion_options = [
    'none',
    'branchala',
    'habbakuk',
    'kiri-jolith',
    'majere',
    'mishakal',
    'paladine',
    'solinari',
    'chislev',
    'gilean',
    'lunitari',
    'reorx',
    'shinare',
    'sirrion',
    'zivilyn',
    'chemosh',
    'hiddukel',
    'morgion',
    'nuitari',
    'sargonnas',
    'takhisis',
    'zeboim',
]

# src: https://rpg.stackexchange.com/questions/125845/what-are-the-official-languages-available-to-players

language_options = [ 
    'common',
    'dwarvish',
    'elvish',
    'giant',
    'gnomish',
    'goblin',
    'halfling',
    'orc',
]

# Strength
# • Athletics

# Dexterity
# • Acrobatics
# • Sleight of Hand
# • Stealth

# Intelligence
# • Arcana
# • History
# • Investigation
# • Nature
# • Religion

# Wisdom
# • Animal Handling
# • Insight
# • Medicine
# • Perception
# • Survival

# Charisma
# • Deception
# • Intimidation
# • Performance
# • Persuasion

background_options = [
    'acolyte', 
    'criminal', 
    'folk hero', 
    'noble', 
    'sage', 
    'soldier',
]

skills_options = [
    'athletics',
    'acrobatics',
    'sleight',
    'stealth',
    'arcana',
    'history',
    'investigation',
    'nature',
    'religion',
    'animal-handling',
    'insight',
    'medicine',
    'perception',
    'survival',
    'deception',
    'intimidation',
    'performance',
    'persuasion',
]

buff_options = [
  {
    'name':'wizard', #  designate the player identifier that will trigger this buff
    'dimension': 'class', # designates which dimension the 'name' option falls under
    'buff': {}, #  designates the character skills or attributes to buff
    'skills':[], # designates character skill proficiencies
  },
    {
    'name':'fighter', 
    'dimension': 'class', 
    'buff': {},
    'skills':[],
  },
  {
    'name':'rogue', 
    'dimension': 'class', 
    'buff': {}, 
    'skills':[],
  },
  {
    'name':'cleric', 
    'dimension': 'class', 
    'buff': {},
    'skills':[],
  },

  { 
    'name':'human', 
    'dimension': 'race', 
    'buff': {'all':1,},
    'skills':[],
  },
  { 
    'name':'elf', 
    'dimension': 'race', 
    'buff': {'dexterity':2,},
    'skills':[],
  },
  { 
    'name':'wood elf',
    'dimension': 'race', 
    'buff': {'dexterity':2, 'wisdom':1,},
    'skills':[],
  },
  { 
    'name':'high elf',
    'dimension': 'race', 
    'buff': {'dexterity':2, 'intelligence':1,},
    'skills':[],
  },
  { 
    'name':'dark elf',
    'dimension': 'race', 
    'buff': {'dexterity':2, 'charisma':1,},
    'skills':[],
  },
  { 
    'name':'dwarf', 
    'dimension': 'race', 
    'buff': {'constitution':2,},
    'skills':[],
  },
  { 
    'name':'hill dwarf',
    'dimension': 'race', 
    'buff': {'constitution':2, 'wisdom':1,},
    'skills':[],
  },
  { 
    'name':'mountain dwarf',
    'dimension': 'race', 
    'buff': {'constitution':2, 'strength':2,},
    'skills':[],
  },
  { 
    'name':'halfling', 
    'dimension': 'race', 
    'buff': {'dexterity':2,},
    'skills':[],
  },
  { 
    'name':'stout halfling',
    'dimension': 'race', 
    'buff': {'dexterity':2, 'constitution':1,},
    'skills':[],
  },
  { 
    'name':'lightfoot halfling',
    'dimension': 'race', 
    'buff': {'dexterity':2, 'charisma':1,},
    'skills':[],
  },
  { 
    'name': 'acolyte', 
    'dimension': 
    'background', 
    'buff': {'all':1,},
    'skills':[],
  },
  { 
    'name': 'criminal', 
    'dimension': 'background', 
    'buff': {'all':1,},
    'skills':[],
  },
  { 
    'name': 'folk hero',
    'dimension': 'background', 
    'buff': {'all':1,},
    'skills':[],
  },
  { 
    'name': 'noble', 
    'dimension': 'background', 
    'buff': {'all':1,},
    'skills':[],
  },
  { 
    'name': 'sage', 
    'dimension': 'background', 
    'buff': {'all':1,},
    'skills':[],
  },
  { 
    'name': 'soldier', 
    'dimension': 'background', 
    'buff': {'all':1,},
    'skills':[],
  },

]
