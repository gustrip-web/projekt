class Monster():
    def __init__(self, name, hp, dmg, lvl): 
        self.hp = hp*(1+lvl/5)
        self.dmg = dmg
        self.name = name
        self.lvl = lvl
