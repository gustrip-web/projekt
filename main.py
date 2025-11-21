from monster import *
import random as rand
from items import *
from character import *

#Characters
tank = Characterclass("Mr.Tank", 200, 10, 0.1, 2)
warrior = Characterclass("Warrior", 100, 25, 0.1, 2)
mage = Characterclass("Magician", 60, 35, 0.2, 1.5)
gambler = Characterclass("Gambler", 100, 1, 0.35, 1000)

#Monster
Monster = [
    Monster("Skeleton", 40, 20,),
    Monster("Goblin", 75, 10),
    Monster("Epstein", 100, 10)
    ]

print("Welcome to the Sweelept")
while True:
    print(""" 
     Read about the Classes:
     1. Warrior               3. Tank
     2. Magiacan              4. Gamblier
     5. Choose your class
     """)
    infosvar = input("Vilken vill du läsa om?")
    if infosvar == "1":
        print("Warrior is ..")
    elif infosvar == "2":
        print("Magican isJN")
    elif infosvar == "3":
        print("Tank is")
    elif infosvar == "4":
        print("Gambler is")
    elif infosvar == "5":
        print(""" 
          Classes:
          1. Warrior               3. Tank
          2. Magiacan              4. Gamblier
          """)
        val = (input("Vilken karaktär vill du välja"))
        if val == "1":
                         playerclass = Warrior
                         break
        elif val =="0":
                         continue
        elif val =="2":
                         playerclass = Magican
                         break
        elif val =="3":
                         playerclass = Tank
                         break
        elif val =="4":
                         playerclass = Gambler
                         break
        else:
                    print("skriv ett tal")
    else:
                    print("skriv ett tal")
playername = input("Vad ska din karaktär heta?")

alive = True
while alive == True:
     print(f"""          Sweelept
 1. Äventyr       2. Markanden       3. Bibloteket

 {lvl}       4. Stats allocation
     
     """)
Platsval = input("Var vill du gå")
if Platsval == 1:
     print("Du har valt att äventyra")

elif Platsval ==2:
     print("Du har valt att gå till markanden")

elif Platsval ==3:
     print("Du har valt att gå till biblloktekt")

elif Platsval ==4:









# li = []



# for i in range(10):
#     m = Monster("goblin", 10, 15, 22)
#     li.append(m)


# healthpotion = Items("Health_potion", 10, 0, 1)
# strengthpotion = Items("strength_potion", 0, 10, 1)


# svärd = Weapon("Long Sword", 25, 1, 1)
