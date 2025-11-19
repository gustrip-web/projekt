from monster import *
import random as rand
from items import *
from character import *

tank = Characterclass("Mr.Tank", 200, 10, 1)
Warrior = Characterclass("Warrior", 100, )


print("Welcome to the swepelt")
while True:
     print(""" 
     Read about the Classes:
     1. Warrior               3. Tank
     2. Magiacan              4. Gamblier
     5. Choose your class
     """)
     infosvar = print(input("Vilken vill du läsa om?"))
     if infosvar == "1":
          print("Warrior is ..")
     elif infosvar == "2":
               print("Magican is")
     elif infosvar == "3":
               print("Tank is")
     elif infosvar == "4":
               print("Gambler is")
     elif infosvar == "5":
          val = print(input("""
          Vad är ditt val? 
          Trcyk 0 noll för att läsa mer
          """))
          if val == 1:
               playerclass = Warrior
          elif val ==2:
               playerclass = Magican
          elif val ==2:
               playerclass = Magican
          
          
Characterclass = input("Choose your Class:")








# li = []



# for i in range(10):
#     m = Monster("goblin", 10, 15, 22)
#     li.append(m)


# healthpotion = Items("Health_potion", 10, 0, 1)
# strengthpotion = Items("strength_potion", 0, 10, 1)


# svärd = Weapon("Snopp", 25, 1, 1)
    
# print(svärd)