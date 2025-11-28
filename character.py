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

        while self.exp >= self.exp_required():
            self.exp -= self.exp_required
            self.lvl += 1
            self.level_up()



    

