from monster import *
import random as rand
from items import *
from character import *
import time

#Characters
tank = Characterclass("Mr.Tank", 200, 10, 0.1, 2)
warrior = Characterclass("Warrior", 100, 25, 0.1, 2)
magi = Characterclass("Magician", 60, 35, 0.2, 1.5)
gambler = Characterclass("Gambler", 100, 1, 0.35, 1000)

# Weapon
Hands = Weapon("Händer", 1 , 0.001 , 1.2 )
weapon_list1 = [Weapon("Svärd", 3, 0.1, 1.5),
Weapon("Dolk",2 , 0.2, 1.5), 
Weapon("Smörkniv", 1.25, 0.25 , 2),
Weapon("Yxa", 4, 0.05, 1.5),
Weapon("Knogjärn", 2, 0.25, 1.25)]

# Items
Item_list1 = [Item("Small_Health_Potion",15 ,0),
Item("Medium_Helth_Potion", 30, 1),
Item("Big_Health_Potion", 60, 1),
Item("Damgae_boost", 0, 1.5)]

#Monster
monster_list1= [Monster("Skeleton", 40, 20, 1), 
    Monster("Goblin",75, 10, 1),
    Monster("Goon", 35, 5, 1),
    Monster("Bandit", 50, 13, 1)]

monster_list2= [Monster("Demon", 175, 28, 1),
    Monster("Troll", 250, 18, 1),
    Monster("Vandrande Själ", 100, 35, 1),
    Monster("Varulv", 200, 23, 1)]
    
monster_list3= [Monter("Jätte", 400, 35, 1),
    Monster("Drake", 300, 45, 1),
    Monster("Skuggriddare", 275, 50, 1),
    Monster("Golem", 450, 20, 1)]

#Gameplay
print("Welcome to the Sweelept")
while True:
    print(""" 
     Read about the Classes:
     1. Warrior               3. Tank
     2. Magiacan              4. Gamblier
     5. Choose your class
     """)
    infosvar = input("Vilken vill du läsa om? ")
    if infosvar == "1":
        print("""
        Född på slagfälten där stål möter storm,
        kan en  Warrior slips till en kompromisslös kombination av kraft,
        disciplin och taktiskt sinne. Deras förfäder vandrade från by till rike som legosoldater,
        vakter och hjältar – men alltid med ett personligt uppdrag som drivit dem vidare.
        Deras styrka ligger i balans: tillräckligt snabba för att slå först,
        tillräckligt tåliga för att överleva, tillräckligt smarta för att anpassa sig.
        För en Warrior är varje strid en chans att bevisa att viljekraft alltid är starkare än ödet
        """)
    elif infosvar == "2":
        print("""
        Magician föddes inte med kraft; de stal den ur kosmos.
        Åratal av studier, förbjudna tomes och riskfyllda ritualer har gett dem förmågan att manipulera eld, rum, tid och energi på avstånd.
        Varje besvärjelse de kastar sliter lite på deras kropp, men deras intellekt och precision gör dem dödligare än de flesta krigare.
        De vandrar världen i jakt på ny kunskap – och på att kontrollera de krafter som lika gärna kan förgöra dem som deras fiender.
        """)
    elif infosvar == "3":
        print("""
        Tank har stått i frontlinjen längre än de vill minnas och bär ärren efter otaliga belägringar.
        De har tränat sina kroppar till att uthärda det ingen annan överlever,
        och deras närvaro får fiender att tveka innan de slår.
        När världen hotas är Tank sista hindret mellan kaos och de oskyldiga – en levande fästning som aldrig ger upp.
        Deras styrka kommer inte bara från muskler, utan från en oböjlig vilja som vägrar låta någon falla bakom dem.
        """)
    elif infosvar == "4":
        print("""
        Gambler föddes med osannolik tur,
        men den välsignelsen visar ofta sina tänder.
        De lever för spänningen i risken: varje slag,
        varje kort, varje beslut är ett spel där universum tycks väga deras öde på en knivsegg.
        Deras strider präglas av vilda svängningar – från förödande kritiska träffar till total kollaps – och de accepterar båda resultaten som en del av spelet.
        Gambler vandrar mellan bord, tavernor och slagfält, alltid jagad av lyckans nyckfulla hand.
        """)
    elif infosvar == "5":
        print(""" 
          Classes:
          1. Warrior               3. Tank
          2. Magiacan              4. Gamblier
          """)
        val = (input("Vilken karaktär vill du välja? "))
        if val == "1":
                         playerclass = warrior
                         break
        elif val =="0":
                         continue
        elif val =="2":
                         playerclass = Mmagi
                         break
        elif val =="3":
                         playerclass = tank
                         break
        elif val =="4":
                         playerclass = gambler
                         break
        else:
                    print("skriv ett tal")
    else:
                    print("skriv ett tal")
playername = input("Vad ska din karaktär heta? ")

alive = True
adventuring=False
Shopping=False
Reading=False

def korsningen():
    plats = rand.randint(1,2,3) #Bestämmer vilken väg som du kommer till
    väghem = rand.randint(1,2)    #Slumpar om du kan komma hem
    if väghem == 1:   #Väg hem finns
        print("Du kommer till en skog där stigen blir till en väg och till två stigar")
        vägval = input("Vilken stig väljer du? 1 = Vägen, 2 = Stig nr1, 3 = Steg nr2")
        if vägval == "1":
            gårhem="ja"
            return        # returnera värdern som player fått under äventyret
        else:
                    print(f"Du går {vägval}")  
    else:
                 print("Du kommer till en skog där stigen blir till tre stigar")
                 vägval = input("Vilken stig väljer du? 1 = Stig , 2 = Stig nr1, 3 = Steg nr2")
                 print(f"Du går {vägval}")  
    return plats, gårhem
def vägdecision():         #Väg val på de olika vägarna
    vägval3 = input("Vill du vända tillbaka= ja eller ner")
    if len(vägval3) == 2:
        vägsvar3 = 1      # Player vill vända tillbaka
    else: vägsvar = 2   #Vill forsätta
    return vägsvar

def monsterpullar():
    monsterval = rand.choice(monster_list1)
    print("Du ser monstret {monsterval.name}")
    return monsterval


def grottvägen():
    print("Efter ett tag kommer du till en Grotta")
    print("Fuktig tunnel med droppande stalaktiter, svagt ljus från utgången bakom dig. Marken är hal och stenig.")
    if vägdecision() ==1:     #Om man vänder så kommer man tillbaka till vägvalet
        return
    else: #Forsätte
        print("Du går ner i grottan")
        monsterval = monsterpullar()
        battle(monsterval, playerclass)
        if alive == False:          # Alive ändras i battle func
            global adventuring 
            adventuring = False
            return              # Om du dör så slutar funk köras
    print("Efter du dödat monsteret går du vidare")
    time.sleep(3)  # import time
    print("Du hinner bara gå ett par minuter innan du hör något mullra, du vänder dig om och ser massor stenar rulla mot dig")
    print("Du lowkey ser ett smaband i stenarna, nummrena 13 98 flashar i din hjärna")
    time.sleep(5)
    os.system('cls')


    
    
    

def skogsvägen():
    pass

    
def abanondedcity():
    pass
    
def adventuring():      #funk som körs när man äventyrar
    print("Du har lämnat byn och går på en väg") #Intro 
    while adventuring == True:
        print("Du kommer till en skog där vägen försvinner till tre stigar")
        plats, gårhem = korsningen()
        if gårhem == "ja":
            adventuring=False
            break      # Slutar while loopen
        if plats == 1:
            grottvägen()
        elif plats == 2:
            skogsvägen()
        elif plats ==3:
            abanondedcity()
        

    return


        # elif  #Skogsvägen 
        # elif  # Abondecnd city
    
while alive == True:
    print(f"""          Sweelept
    1. Äventyr       2. Markanden       3. Bibloteket

    {lvl}       4. Stats allocation
        
        """)
    Platsval = input("Var vill du gå")
    if Platsval == "1":
        print("Du har valt att äventyra") 
        adventuring = True
        pass
        

    elif Platsval ==2: 
        print("Du har valt att gå till markanden")

    elif Platsval ==3:
        print("Du har valt att gå till biblloktekt")

    elif Platsval ==4:
        print("gå till markanden")

    elif Platsval ==3:
        print("Du har valt att gå till biblloktekt")

    elif Platsval ==4:
        pass
    
def battle(battling_monster, batteling_character):

    while Characterclass.hp > 0 and Monster.hp > 0:
        
        battlec = input(f"Vad vill du göra?   Ditt liv{batteling_character.hp}hp,          Monstrets liv {battling_monster.hp} \n   1 Attackera     2. Heala    3. Försök att fly")
        if battlec == "1": 
            
            dmg = batteling_character.str * batteling_character.weapon.damage
            
            all_critrate = batteling_character.critrate + batteling_character.weapon.critrate
            if rand.random() <= all_critrate:
                dmg *= batteling_character.crit_damage * batteling_character.weapon.crit_damage
            
            batteling_monster.Monster.hp -= dmg
            Print("Du skadade {Monster.name} med {Characterclass.str}! Nu har {Monster.name} {Monster.hp} hp kvar.")
        elif battlec == "2": 
            pass
                 # Heal
        
        elif battlec == "3": 
            flybattle = rand.randint(1,2)
            if flybattle == 1:
                return
        else:
            pass

        if Monster.hp <= 0:
            print("Du dödade monstret!")
            reward = battling_monster.exp_reward()
            batteling_character.add_exp(exp)
            return

        batteling_character.Characterclass.hp -= batteling_character.Monster.dmg

        if Characterclass.hp <= 0:
            print("Du blev besegrad av monstret!")
            global alive
            alive = False
            return
        



# li = []



# for i in range(10):
#     m = Monster("goblin", 10, 15, 22)
#     li.append(m)


# healthpotion = Items("Health_potion", 10, 0, 1)
# strengthpotion = Items("strength_potion", 0, 10, 1)


# svärd = Weapon("Snopp", 25, 1, 1)
    
# print(svärd)