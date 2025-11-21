from monster import *
import random as rand
from items import *
from character import *

#Characters
tank = Characterclass("Mr.Tank", 200, 10, 0.1, 2, 1)
warrior = Characterclass("Warrior", 100, 25, 0.1, 2, 1)
mage = Characterclass("Magician", 60, 35, 0.2, 1.5, 1)
gambler = Characterclass("Gambler", 100, 1, 0.35, 1000, 1)

#Monster
skeleton=Monster("Skeleton", 40, 20, )
goblin=Monster("Goblin",75, 10, )


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
        print("Född på slagfälten där stål möter storm, kan en  Warrior slips till en kompromisslös kombination av kraft, disciplin och taktiskt sinne. Deras förfäder vandrade från by till rike som legosoldater, vakter och hjältar – men alltid med ett personligt uppdrag som drivit dem vidare. Deras styrka ligger i balans: tillräckligt snabba för att slå först, tillräckligt tåliga för att överleva, tillräckligt smarta för att anpassa sig. För en Warrior är varje strid en chans att bevisa att viljekraft alltid är starkare än ödet")
    elif infosvar == "2":
        print("Magician föddes inte med kraft; de stal den ur kosmos. Åratal av studier, förbjudna tomes och riskfyllda ritualer har gett dem förmågan att manipulera eld, rum, tid och energi på avstånd. Varje besvärjelse de kastar sliter lite på deras kropp, men deras intellekt och precision gör dem dödligare än de flesta krigare. De vandrar världen i jakt på ny kunskap – och på att kontrollera de krafter som lika gärna kan förgöra dem som deras fiender.")
    elif infosvar == "3":
        print("Tank har stått i frontlinjen längre än de vill minnas och bär ärren efter otaliga belägringar. De har tränat sina kroppar till att uthärda det ingen annan överlever, och deras närvaro får fiender att tveka innan de slår. När världen hotas är Tank sista hindret mellan kaos och de oskyldiga – en levande fästning som aldrig ger upp. Deras styrka kommer inte bara från muskler, utan från en oböjlig vilja som vägrar låta någon falla bakom dem.")
    elif infosvar == "4":
        print("Gambler föddes med osannolik tur, men den välsignelsen visar ofta sina tänder. De lever för spänningen i risken: varje slag, varje kort, varje beslut är ett spel där universum tycks väga deras öde på en knivsegg. Deras strider präglas av vilda svängningar – från förödande kritiska träffar till total kollaps – och de accepterar båda resultaten som en del av spelet. Gambler vandrar mellan bord, tavernor och slagfält, alltid jagad av lyckans nyckfulla hand.")
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
adventuring=False
Shopping=False
Reading=False
def adventuring():
    print("Du har valt att äventyra")
    adventuring = True
    print("Du har lämnat byn och går på en väg")
    print("Du kommer till en skog där vägen försvinner till tre stigar")
    while adventuring == True:
            plats = rand.choice(1,2,3)
            väghem = rand.choice(1,2)
            if vägen == 1:   #Väg hem finns
                print("Du kommer till en skog där stigen blir till en väg och till två stigar")
                vägval = input("Vilken stig väljer du? 1 = Vägen, 2 = Stig nr1, 3 = Steg nr2")
                if vägval == "1":
                    break
                else:
            else:
                print("Du kommer till en korsning där stigen blir till tre stigar")
                vägval = input("Vilken stig väljer du?")
            print(f"Du går {vägval}")
            if plats == 1:  #Grottvägen
                vägval2 = input("Efter ett tag kommer du till en Grotta vill du gå ner? ja / nej")
                vägval = vägval.lower()
                if len(vägval) == 2:
                    "Du går ner i grottan"
                else:
                    print("Du vänder tillbaka")



        elif  #Skogsvägen 
        elif  # Abondecnd city
    
while alive == True:
    print(f"""          Sweelept
    1. Äventyr       2. Markanden       3. Bibloteket

    {lvl}       4. Stats allocation
        
        """)
    Platsval = input("Var vill du gå")
    if Platsval == "1":
        
        

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


# svärd = Weapon("Snopp", 25, 1, 1)
    
# print(svärd)