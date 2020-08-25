import pandas as pd
import defaults # this is where we store the default dimensions

# add support for default, graphical, and random generation


class Mercutio:
    def __init__(self):
        self.cls_options = defaults.class_options
        self.attribute_options = defaults.attribute_options
        self.race_options = defaults.race_options
        self.religion_options = defaults.religion_options
        self.language_options = defaults.language_options
        self.special_options = defaults.special_options
        
    def gen(self, cls=None, attributes=None, race=None, religion=None, language=None, specials=None):
        pass

    def load(self, how='append', cls=None, attributes=None, race=None, religion=None, language=None, specials=None):
        pass

    def to_csv(self):
        pass

    def read_csv(self):
        pass

