import pandas as pd
import defaults # this is where we store the default dimensions
import pickle

# add support for default, graphical, and random generation


class Mercutio:
    def __init__(self):
        self.player_class_options = defaults.player_class_options
        self.attribute_options = defaults.attribute_options
        self.race_options = defaults.race_options
        self.religion_options = defaults.religion_options
        self.language_options = defaults.language_options
        self.special_options = defaults.special_options
        
    def gen(self, player_class=None, attributes=None, race=None, religion=None, language=None, specials=None):
        
        if player_class:
            if player_class in self.player_class_options:
                self.player_class = player_class
        else: self.player_class = ''

        if attributes:
            if attributes in self.attributes_options:
                self.attributes = attributes
        else: self.attributes = ''

        if race:
            if player_race in self.race_options:
                self.race = race
        else: self.race = ''

        if religion:
            if religion in self.religion_options:
                self.religion = religion
        else: self.religion = ''

        if language:
            if language in self.language_options:
                self.language = language
        else: self.language = ''

        if special:
            if special in self.special_options:
                self.special = special
        else: self.special = ''



    def load(self, how='append', cls=None, attributes=None, race=None, religion=None, language=None, specials=None):
        pass

    def to_csv(self):
        pass

    def read_csv(self):
        pass

