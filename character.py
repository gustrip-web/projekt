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

    def exp_required(self):
        return int(100 * (1.2 ** (self.lvl - 1)))

    def level_up(self):
        self.lvl += 1
        self.str *= 1.10
        self.hp *= 1.01
        print(f"{self.name} levla upp till {self.lvl}!")
    
    def add_exp(self, reward):
        self.exp += reward

        while self.exp >= 100:
            self.exp -= (100*(1.2**self.lvl))
            self.lvl += 1
            self.character_damage()
            self.character_hp()



Player1.character_damage() * svärd.damage()
    

