from items import *
import random as rand

class Characterclass():
    def __init__(self, name, hp, str, critrate, crit_damage):
        self.name = name
        self.hp = hp
        self.str = str
        self.lvl = 1
        self.exp = 0
        self.money = 0
        self.crit_damage = crit_damage
        self.critrate = critrate
        self.weapon = None
        self.alive = True
        self.hybris= False
        self.skog = False
        self.grott = False
        self.city = False

        self.inventory = []

    def exp_required(self):
        return int(100 * (1.2 ** (self.lvl - 1)))

    

    
        

    def level_up(self):
        self.lvl += 1
        self.str *= 1.10
        self.hp *= 1.05
        print(f"{self.name} levla upp till {self.lvl}!")

    def levelups(self, xp):
        if xp == 0:
            print(f"Du är lvl {self.lvl}")
        
        if xp > 0:
            slowtype(f"Du fick {xp} xp")
        totxp = xp + self.xp
        lvlupexp = self.lvl*self.lvl
        while totxp < lvlupexp:
            level_up()
            totxp -= lvlupexp
            lvlupexp = self.lvl*self.lvl
        
    
    def add_exp(self, reward):
        self.exp += reward
        while self.exp >= self.exp_required():
            self.exp -= self.exp_required()
            self.lvl += 1
            self.level_up()
    
    def amoney(self, belopp):
        self.money += belopp
        print(f" Du har nu {self.money} pengar")
        


# INVENTORY
    def add_item(self, item):
        self.inventory.append(item)
        print(f"Du plockade upp: {item.name}")

    def show_inventory(self):
        if not self.inventory:
            print("Inventory är tomt.")
            return

        print("\n--- INVENTORY ---")
        for i, item in enumerate(self.inventory, start=1):
            print(f"{i}. {item.name} (+{item.health_boost} HP, +{item.damage_boost} DMG)")
        print("------------------\n")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.hp += item.health_boost
                self.str += item.damage_boost
                print(f"Du använde {item.name}!")
                print(f"Ny HP: {self.hp}, Ny DMG: {self.str}")
                self.inventory.remove(item)
                return
        print("Du har inte det föremålet!")