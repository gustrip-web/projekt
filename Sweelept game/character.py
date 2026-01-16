from items import *
import random as rand
import time

def slowtype(text, tid):
    for a in text:
        print(a, end="", flush=True)   # End hindrar nyrad,    flush låter termineln skriva ut induviduella tecken innan hela raden är klar
        time.sleep(tid)
    print("\n")

class Characterclass():
    def __init__(self, name, hp, str, critrate, crit_damage):
        self.name = name
        self.pname = None
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
        return int(20 * (1.5 ** (self.lvl - 1)))    # Switcha denna för mer balnce och jämnare tal vi lvl ups
                                                    #ökar antalet exp som behövs för att lvla upp för att göra spelet lite svårare

    def level_up(self):
        self.lvl += 1                       #spelaren tjänar en extra lvl på de lvlarna hen redan hadde
        newstr = self.str * 1.10               #för varje lvl så ökar spelarens dmg med 10%
        self.str = round(newstr)                #rundar av dmg för att undvika många decimaler
        newhp = self.hp * 1.10                      #höjer hp med 10% varje lvl
        self.hp = round(newhp)                      #rundar av för att undvika deciamler
        slowtype(f"{self.name} levla upp till {self.lvl}!",.05)     #informerar spelaren om att hen har levlat upp
        slowtype(f"Din bas skada {self.str}", 0.05)                 #informerar spelaren om dess nya skada

    def add_exp(self, reward):
        self.exp += reward                             #spelaren får exp som plussas på expen spelaren redan hadde
        while self.exp >= self.exp_required():          #kollar om spelaren har mer exp än vad som behövs för att lvla upp
            self.exp -= self.exp_required()                #om den har det så subtraheras antalet exp som behövs för att lvla upp och resten kan användas till nästa lvl
            self.level_up()                         #spelaren lvlar upp
    
    def amoney(self, belopp):
        self.money += belopp                                #spelaren får pengar som adderas på summan av spelarens plånbok
        slowtype(f"Du har nu {self.money} pengar",0.05)            #visar spelaren antal pengar hen nu har
        


# INVENTORY
    def add_item(self, item):
        self.inventory.append(item)                             #lägger in item i self.inventory
        slowtype(f"Du plockade upp: {item.name}",0.05)              #informerar spelaren om att den har plockat upp vapen

    def show_inventory(self):
        if not self.inventory:                          #kollar om det inte finns någonting i inventory
            slowtype("Inventory är tomt.", 0.05)            #om det inte finns printas ut att det är tomt
            return

        slowtype("\n--- INVENTORY ---",0.01)        
        for i, item in enumerate(self.inventory, start=1):                                  #enumerate räknar alla items i listan och ger infon till i som börjar på 1
            slowtype(f"{i}. {item.name} (+{item.health_boost} HP, *{item.damage_boost} DMG)",0.01)      #i säger vilket nummer itemet har i inventoryt sedan sägs namnet på itemet samnt hur mycket hp som adderas och hur mycket damage multipliceras med beroende på item
        slowtype("------------------\n",0.01)
    
    def show_weapon(self):
        slowtype(f"Ditt vapen är {self.weapon.name}",0.05)      #visar ditt nuvarande vapen i inv

    def use_item(self, item_name):
        for item in self.inventory:                             #går igenom spelarens items
            if item.name.lower() == item_name.lower():             #kollar så att itemet som spelaren har skrivit att de vill använda matchar med items den har
                self.hp += item.health_boost 
                self.hp = round(self.hp)               #hp adderas
                self.str *= item.damage_boost   
                self.str = round(self.str)            #damage multipliceras
                slowtype(f"Du använde {item.name}!",0.05)       #Säger namnet på itemet du använde
                slowtype(f"Ny HP: {self.hp}, Ny DMG: {self.str}",0.05)          #informerar spelaren om nya stats
                self.inventory.remove(item)                 #tar bort itement ur inv eftersom att den bara ska användas 1 gång

                return                                          #skickar all info till spelaren
        slowtype("Du har inte det föremålet!",0.05)                 #om namnet på föremålet som spelaren vill använda inte matchar med något av itemsen som spelaren har printas detta