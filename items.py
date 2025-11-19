class Weapon():
    def __init__(self, name, damage, critrate, crit_damage, lvl):
        self.name = name
        self.damage = damage
        self.critrate = critrate
        self.crit_damage = crit_damage
        self.lvl = lvl
    
    def sword_damage(self):
        dmg = self.damage *(1.1 ** (self.lvl-1))
    
    def crit_attack(self):
        dmg *= self.crit_damage
    
    def lvl_up(self):
        self.lvl += 1





class Items():
    def __init__(self, name, health_boost, damage_boost, lvl):
        self.health_boost = health_boost
        self.damage_boost = damage_boost
        self.lvl = lvl
        self.name = name
    
