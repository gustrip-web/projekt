class Monster():
    def __init__(self, name, hp, dmg, lvl): 
        self.hp = hp*(1+lvl/5)
        self.dmg = dmg
        self.name = name
        self.lvl = lvl

def nivå():
    lvl += nivå

Monster_list = [    golem = Monster("Golem" , 100, 20, 1)
    goblin = Monster("Goblin", 25, 5, 1)]

print(f"Ditt monster har {golem.hp} hp")
