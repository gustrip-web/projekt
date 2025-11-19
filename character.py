from items import *

class Characterclass():
    def __init__(self, name, hp, str, lvl, range = False):
        self.name = name
        self.hp = hp
        self.str = str
        self.range = range
        self.lvl = lvl
    
    def character(self):
        true_dmg = str * dmg