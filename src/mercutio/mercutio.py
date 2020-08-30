import mercutio.defaults as defaults # this is where we store the default dimensions
import pickle

class Player:
    def __init__(self):
        self.player_class_options = defaults.player_class_options
        self.attributes_options = defaults.attributes_options
        self.race_options = defaults.race_options
        self.religion_options = defaults.religion_options
        self.language_options = defaults.language_options
        self.special_options = defaults.special_options
        ### NEED TO ADD SUPPORT FOR SKILLS, EQUIPMENT, ALIGMENT, SPELLS, ATTACKS

    def gen_graphic(self):

        title = [
        '                            _   _       ',
        '  /\/\   ___ _ __ ___ _   _| |_(_) ___  ',
        " /    \ / _ \ '__/ __| | | | __| |/ _ \ ",
        '/ /\/\ \  __/ | | (__| |_| | |_| | (_) |',
        '\/    \/\___|_|  \___|\__,_|\__|_|\___/ ',
        ]

        for item in title:print(item)

        print('\nWelcome to the graphical player generator. Please follow the instructions below.\n')

        if not hasattr(self, 'name'):
            self.name = input('Please enter your desired username: ')

        if not hasattr(self, 'player_class'):
            while True:    
                self.player_class = input(f'Please enter your desired class -- your options are {self.player_class_options}: ')
                if self.player_class in self.player_class_options: break

        if not hasattr(self, 'race'):
            while True:    
                self.race = input(f'Please enter your desired race -- your options are {self.race_options}: ')
                if self.race in self.race_options: break

        ### NEED TO ADD SUPPORT FOR RELIGION AND LANGUAGE

    def gen(self, graphical=None, player_class=None, attributes=None, race=None, religion=None, language=None, special=None, name='', level=1):

        if graphical:
            self.gen_graphic()

        if not hasattr(self, 'name'):
            if name: self.name = name
            else: self.name = ''

        if not hasattr(self, 'player_class'):
            if player_class:
                if player_class in self.player_class_options:
                    self.player_class = player_class
            else: self.player_class = ''

        if not hasattr(self, 'race'):
            if race:
                if race in self.race_options:
                    self.race = race
            else: self.race = ''

        self.attributes = {}
        if isinstance(attributes, (dict)):
            for key in attributes:
                if key in self.attributes_options:
                    self.attributes[key] = attributes[key]
        # in the absence of designated attributes, default to 3
        else: 
            for x in self.attributes_options:
                self.attributes[x] = 3

        if not hasattr(self, 'religion'):
            if religion:
                if religion in self.religion_options:
                    self.religion = religion
            else: self.religion = ''

        if not hasattr(self, 'language'):
            if language:
                if language in self.language_options:
                    self.language = language
            else: self.language = ''

        if not hasattr(self, 'special'):
            if special:
                if special in self.special_options:
                    self.special = special
            else: self.special = ''

        if isinstance(level, (int)):
            self.level = level
        else: self.level = 1

        print(f'\nSuccessfully created player: \nname: {self.name}\nclass: {self.player_class}\nattributes: {self.attributes}\nrace: {self.race}\nlanguage: {self.language}\nreligion: {self.religion}\nspecial: {self.special}\n')

    def load_dimensions(self, how='append', player_class=None, attributes=None, race=None, religion=None, language=None, special=None):
        if how == 'overwrite':
            if isinstance(player_class, (list)):
                self.player_class_options = player_class
            if isinstance(attributes, (list)):
                self.attributes_options = attributes
            if isinstance(race, (list)):
                self.race_options = race
            if isinstance(religion, (list)):
                self.religion_options = religion
            if isinstance(language, (list)):
                self.language_options = language
            if isinstance(special, (list)):
                self.special_options = special
        elif how == 'append': 
            if isinstance(player_class, (list)):
                [self.player_class_options.append(x) for x in player_class]
            if isinstance(attributes, (list)):
                [self.attributes_options.append(x) for x in attributes]
            if isinstance(race, (list)):
                [self.race_options.append(x) for x in race]
            if isinstance(religion, (list)):
                [self.religion_options.append(x) for x in religion]
            if isinstance(language, (list)):
                [self.language_options.append(x) for x in language]
            if isinstance(special, (list)):
                [self.special_class_options.append(x) for x in special]

    def save(self):
        filename = f'{self.name}.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(vars(self), f)
        print(f'\nSuccessfully saved player data to {filename}\n')

    def load_player(self, filename):
        try: 
            loaded_file = pickle.load(open(filename, "rb"))

            self.player_class = loaded_file['player_class']
            self.attributes = loaded_file['attributes']
            self.race = loaded_file['race']
            self.religion = loaded_file['religion']
            self.language = loaded_file['language']
            self.special = loaded_file['special']
            self.name = loaded_file['name']
            self.level = loaded_file['level']

            print(f'\nSuccessfully loaded {filename} player data\n')

        except: print(f'\nNo player data found at {filename}\n')


    def mod(self, player_class=None, attributes=None, race=None, religion=None, language=None, special=None, name=None, level=None):
        if hasattr(self, 'name'): # this asserts that self.name has been set, meaning the user has run gen() or load_player()
            if player_class:
                if player_class in self.player_class_options:
                    self.player_class = player_class
            
            if isinstance(attributes, (dict)):
                for key in attributes:
                    if key in self.attributes_options:
                        self.attributes[key] = attributes[key]
            if race:
                if race in self.race_options:
                    self.race = race

            if religion:
                if religion in self.religion_options:
                    self.religion = religion

            if language:
                if language in self.language_options:
                    self.language = language

            if special:
                if special in self.special_options:
                    self.special = special

            if name: self.name = name

            if isinstance(level, (int)):
                self.level = level

            print(f'\nSuccessfully modified player: \nname: {self.name}\nclass: {self.player_class}\nattributes: {self.attributes}\nrace: {self.race}\nreligion: {self.religion}\nspecial: {self.special}\n')
        else: 
            print('\nNo player has been loaded or generated.\nPlease gen() or load_player() before modifying your player')