from items import *
import random as rand

class Characterclass():
    def __init__(self, name, hp, str, critrate, crit_damage, lvl):
        self.name = name
        self.hp = hp
        self.str = str
        self.lvl = lvl
        self.crit_damage = crit_damage
        self.critrate = critrate

    def character_damage(self):
        dmg = self.str *(1.1 ** (self.lvl-1))

        if rand.random(0.0, 1.0) <= critrate:
            dmg *= self.crit_damage
            return dmg, True
        return dmg, False
    
    def character_hp(self):
        self.hp *= (1.01**(self.lvl-1))
    
    def add_exp(self, amount):
        self.lvl += amount

    
    def character(self):
        true_dmg = str * dmg

Player1.character_damage() * svärd.damage()
    