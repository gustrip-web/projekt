class Weapon():
    def __init__(self, name, damage, critrate, lvl):
        self.name = name
        self.damage = damage
        self.critrate = critrate
        self.lvl = lvl
    
    def sword_damage(self):
        return self.damage *(1.1 ** (self.lvl-1))
    
    def crit_attack(self):
        return self.damage **2
    
    def lvl_up(self):
        self.lvl += 1





class Items():
    def __init__(self, name, health_boost, damage_boost, lvl):
        self.health_boost = health_boost
        self.damage_boost = damage_boost
        self.lvl = lvl
        self.name = name