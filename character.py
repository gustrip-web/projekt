from items import *
import random as rand

class Characterclass():
    def __init__(self, name, hp, str, critrate, crit_damage):
        self.name = name
        self.hp = hp
        self.str = str
        self.lvl = 1
        self.exp = 0
        self.crit_damage = crit_damage
        self.critrate = critrate

    def character_damage(self):
        self.str *= (1.1 ** (self.lvl-1))

        if rand.random() <= self.critrate:
            self.str *= self.crit_damage
    
    def character_hp(self):
        self.hp *= (1.01**(self.lvl-1))
    
    def add_exp(self, amount):
        self.exp += amount

        while self.exp >= 100:
            self.exp -= (100*(1.2**self.lvl))
            self.lvl += 1
            self.character_damage()
            self.character_hp()

    




    

Player1.character_damage() * svärd.damage()
    