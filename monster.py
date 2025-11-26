import random as rand
class Monster():
    def __init__(self, name, hp, dmg, lvl): 
        self.lvl = lvl
        self.hp = hp*(1+self.lvl/5)
        self.dmg = dmg*(1+self.lvl/5)
        self.name = name

    def attack(self,target):
        print(f"{self.name} attackerade dig och gjorde {self.dmg} skada!")
        target.hp -= self.dmg
        if target.hp <=0:
            target.hp = 0
            print(f"{self.name} dödade dig!")
            return True
        return false



    def exp_reward(self):
        return rand.randint(10,35)