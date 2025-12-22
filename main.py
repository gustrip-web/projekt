# SÄTT TILL
from monster import *
import random as rand
from items import *
from character import *
import time

# Characters
tank = Characterclass("Mr.Tank", 200, 10, 0.1, 2)
warrior = Characterclass("Warrior", 100, 25, 0.1, 2)
magi = Characterclass("Magician", 60, 35, 0.2, 1.5)
gambler = Characterclass("Gambler", 100, 1, 0.35, 1000)

# Weapon
Hands = Weapon("Händer", 1, 0.001, 1.2)
weapon_list1 = [Weapon("Svärd", 3, 0.1, 1.5),
                Weapon("Dolk", 2, 0.2, 1.5),
                Weapon("Smörkniv", 1.25, 0.9, 1000),
                Weapon("Yxa", 4, 0.05, 1.5),
                Weapon("Knogjärn", 2, 0.25, 1.25)]

BackseatWeapon = Weapon("Golfklubba", 5, 0.30, 1.4)

# Items
Item_list1 = [Item("Small_Health_Potion", 15, 1),
              Item("Medium_Helth_Potion", 30, 1),
              Item("Big_Health_Potion", 60, 1),
              Item("Damage_boost", 0, 1.1)]

# Monster
monster_list1 = [Monster("Skeleton", 40, 20, 1),
                 Monster("Goblin", 75, 10, 1),
                 Monster("Goon", 35, 5, 1),
                 Monster("Bandit", 50, 13, 1)]

monster_list2 = [Monster("Demon", 175, 28, 1),
                 Monster("Troll", 250, 18, 1),
                 Monster("Vandrande Själ", 100, 35, 1),
                 Monster("Varulv", 200, 23, 1)]

monster_list3 = [Monster("Jätte", 400, 35, 1),
                 Monster("Drake", 300, 45, 1),
                 Monster("Skuggriddare", 275, 50, 1),
                 Monster("Golem", 450, 20, 1)]

sandworm = Monster("Sandworm", 124, 24, 1)

# Gameplay
print("""
         Welcome to the Sweelept!""")
while True:
    print(""" 
     Read about the Classes:
     1. Warrior               3. Tank
     2. Magiacan              4. Gambler
     
            5. Choose your class
     """)
    
    infosvar = input("Vad vill du göra? ")
    
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
          2. Magiacan              4. Gambler
          """)
        
        val = (input("Vilken karaktär vill du välja? "))
        
        if val == "1":
            playerclass = warrior
            print("Du valde klassen Warrior!")
            break
        elif val == "0":
            continue
        elif val == "2":
            playerclass = magi
            print("Du valde klassen Magician!")
            break
        elif val == "3":
            playerclass = tank
            print("Du valde klassen Tank!")
            break
        elif val == "4":
            playerclass = gambler
            print("Du valde klassen Gambler!")
            break
        else:
            print("skriv ett tal")
    else:
        print("skriv ett tal")

playername = input("Vad ska din karaktär heta? ")
print(f"Du valde namnet {playername}!")
alive = True
adventuring = False
Shopping = False
Reading = False

Player_weapon = Hands


def korsningen():
    plats = rand.randint(1, 3)  # Bestämmer vilken väg som du kommer till
    väghem = rand.randint(1, 2)  # Slumpar om du kan komma hem
    if väghem == 1:  # Väg hem finns
        print("Du kommer till en skog där stigen blir till en väg och till två stigar")
        time.sleep(2)
        vägval = input(
            "Vilken stig väljer du? 1 = Vägen, 2 = Stig nr1, 3 = Steg nr2")
        if vägval == "1":
            gårhem = "ja"
            return gårhem    # returnera värdern som player fått under äventyret
        else:
            print(f"Du går {vägval}")
    else:
        print("Du kommer till en skog där stigen blir till tre stigar")
        time.sleep(2)
        vägval = input(
            "Vilken stig väljer du? 1 = Stig , 2 = Stig nr1, 3 = Steg nr2")
        time.sleep(2)
        print(f"Du går {vägval}")
    return plats

def vägdecision():  # Väg val på de olika vägarna
    vägval3 = input("Vill du vända tillbaka? ja eller nej")
    if len(vägval3) == 2:
        vägsvar3 = 1      # Player vill vända tillbaka
    else:
        vägsvar = 2  # Vill forsätta
    return vägsvar

def Markanden():
    playerclass.amoney(20)
    print("vällkomen till markanden")
    while True:
        time.sleep(2)
        print(f""" Vad vill du kolla på?        DU har {playerclass.money} guld
        Vapen: 1. Svärd      Damage: 3     Crit factor: 5/10    Pris: 30 guld
            2. Dolk          Damage: 2     Crit factor: 6/10    Pris: 20 guld
            3. Smörknikv     Damage: 1,05  Crit factor: 2/10    Pris: 5 guld
            4. Yxa           Damage: 4     Crit factor: 2/10    Pris: 40 guld
            5. Knogjärn      Damage: 2     Crit factor: 7/10    Pris: 30 guld

        Items: 6. Small Health Potion    + 15 Hp            Pris: 10 guld
               7. Medium Helth Potion    + 30 Hp            Pris: 20 guld
               8. Big Health Potion      + 60 Hp            Pris: 30 guld
               9. Damage boost           10 % Damage boost  Pris: 40 guld

               q. Lämna affären
        """)
        köpval = input("Vad vill du köpa")
        time.sleep(2)
        if köpval == "1":   #Svärd
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                Vapen = weapon_list1[0]
                playerclass.weapon = Vapen
                print(f"Ditt nya vapen är ett Svärd!")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "2":  #dolk
            if playerclass.money >= 20:
                playerclass.amoney(-20)
                Vapen = weapon_list1[0]
                playerclass.weapon = Vapen
            print("Ditt nya vappen är en Dolk")
        elif köpval == "3":  #Smörkniv
            if playerclass.money >= 10:
                playerclass.amoney(-10)
                Vapen = weapon_list1[1]
                playerclass.weapon = Vapen
                print("Ditt nya vappen är Smörkniv")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "4":   #YXA
            if playerclass.money >= 40:
                playerclass.amoney(-40)
                Vapen = weapon_list1[2]
                playerclass.weapon = Vapen
                print("Ditt nya vappen är Yxa")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "5":    #Knogjärn
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                Vapen = weapon_list1[30]
                playerclass.weapon = Vapen
                print("Ditt nya vappen är Knogjärn")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "6":
            if playerclass.money >= 10:
                playerclass.amoney(-10)
                playerclass.add_item(Item_list1[0])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "7":
            if playerclass.money >= 20:
                playerclass.amoney(-20)
                playerclass.add_item(Item_list1[1])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "8":
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                playerclass.add_item(Item_list1[2])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "9":
            if playerclass.money >= 40:
                playerclass.amoney(-40)
                playerclass.add_item(Item_list1[3])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "q":
            break
        else:
            continue
    return 

def spin_number():
    n = 0.008
    for delay in [n]*129:
        o = rand.randint(1, 4)      
        if o == 1:
            b = "🍒"         
        elif o == 2:
            b = "🔔" 
        elif o == 3:
            b = "🍋"
        elif o == 4:
            b = "💎"

        print(f"\rSpinning: {b}", end=""  , flush=True)
        time.sleep(n)
        n += n*n


    if o == 1:
            b = "🍒"         
    elif o == 2:
            b = "🔔" 
    elif o == 3:
            b = "🍋"
    elif o == 4:
            b == "💎"
    print(f"\rResult:   {b} ")
    return b

def slots():
    slowtype("Välkomen till slotsen", 0.1)
    slowtype("Slots är ett awesome sätt att vinna pengar på", 0.1)
    slowtype("Du måste få tre av samma nummer för att kamma in stor vinsten som är 50", 0.1)
    slowtype("varje spin kostar 5 guld", 0.1)
    while True:
        print(f"Du har {playerclass.money} guld")
        if playerclass.money >= 1:
            slot = input("Vill du spinna? Ja / nej")
            if slot == "nej":           # Gjort med mening för just här måste man säga exact rätt för att dra
                slowtype("kom tillbaka tills slots snart, nästa vinst är bara ett drag ifrån!", 0.1)
            else: 
                playerclass.amoney(-5)
                slot1 = spin_number()
                slot2 = spin_number()
                slot3 = spin_number()
        
            if slot1 == slot2 and slot2 == slot3:
                print("Du vann")
                playerclass.amoney(50)
            else:
                print("Du förlora")
        else:
            print("Du har för lite pengar")
            break
    return

def casion():
    slowtype("Välkomen till casionot", 0.1)
    while True:
        slowtype(f""" Vad vill du göra?     Du har {playerclass.money} guld \n
              1. Slots   2. Spela Black Jack    3. Baren   \n
              4. Poker            5. Quiz                6. Gå tillbaka""", 0.1)
        casval = input("Vad vill du göra?")
        if casval == "1":
            slowtype("Du har valt att spela slots", 0.1)
            slots()
        elif casval == "2":
            slowtype("Du har valt att spela Black Jack", 0.1)
        elif casval == "3":
            slowtype("Du har valt att gå till baren", 0.1)
        elif casval == "4":
            slowtype("Du har valt att spela Poker", 0.1)
        elif casval == "5":
            slowtype("Du har valt att spela Quiz", 0.1)
        elif casval == "6":
            break

def vägescape():  # Väg val på de olika vägarna
    vägval4 = input("Vill du gå vänster eller höger?")
    if len(vägval3) == 6:
        vägsvar3 = 1      # Player vill gå vänstern
    else:
        vägsvar = 2  # Vill gå höger
    return vägsvar


def monsterpullar():
    if playerclass.lvl < 5:
        monsterlista = monster_list1
    elif playerclass.lvl >= 5 and playerclass.lvl < 10:
        monsterlista = monster_list2
    else:
        monsterlista = monster_list3
    monsterval = rand.choice(monsterlista)
    print(f"Du ser monstret {monsterval.name}")
    return monsterval

def slowtype(text, tid):
    for a in text:
        print(a, end="", flush=True)   # End hindrar nyrad,    flush låter termineln skriva ut induviduella tecken innan hela raden är klar
        time.sleep(tid)
    print("\n")



def battle(monsterval, playerclass, alive):
    while playerclass.hp > 0 and monsterval.hp > 0:

        battlec = input(f"""Vad vill du göra?   Du har {playerclass.hp} hp,
        {monsterval.name} har {monsterval.hp} hp
        1. Attackera
        2. Heala
        3. Försök att fly """)

        if battlec == "1":

            dmg = playerclass.str * playerclass.weapon.damage

            all_critrate = playerclass.critrate + playerclass.weapon.critrate
            if rand.random() <= all_critrate:
                dmg *= playerclass.crit_damage * playerclass.weapon.crit_damage
                print(f"Du fick en crit!, nu gör du {dmg} skada")
            else:
                print(f"Du attackerar och gör {dmg} skada")

            monsterval.hp -= dmg
            print(
                f"Du skadade {monsterval.name} med {dmg}! Nu har {monsterval.name} {monsterval.hp} hp kvar.")
        elif battlec == "2":
            pass
        # Heal

        elif battlec == "3":
            if rand.randint(1, 2) == 1:
                print("Du flydde från Monstret(fegis)")
                return
            else:
                print("Du misslyckades att fly")

        else:
            print("Skriv 1, 2 eller 3")
            continue

        if monsterval.hp <= 0:
            print("Du dödade monstret!")
            time.sleep(1)
            print(f"Du tjänade {monsterval.exp_reward} exp och fick {monsterval.money_reward} guld")
            reward = monsterval.exp_reward()
            playerclass.add_exp(reward)
            belopp = monsterval.money_reward()
            playerclass.amoney(reward)
            
            
            return
        print(f"{monsterval.name} attackerar dig och gör {monsterval.dmg} skada!")
        playerclass.hp -= monsterval.dmg
        print(f"Nu har du {playerclass.hp}hp kvar")

        if playerclass.hp <= 0:
            print("Du blev besegrad av monstret!")
            playerclass.alive = False
            return playerclass

def grottvägen(alive):
    print("Efter att gått på stigen en tag kommer du fram till en grott öppning")
    time.sleep(2)

    print("Du kikar ner i den, grottan ser fuktig ut och har droppande stalaktiter")
    if vägdecision() == 1:  # Om man vänder så kommer man tillbaka till vägvalet
        return
    else:  # Forsätte
        print("Du går ner i grottan")
        time.sleep(2)
        print("Det är brant och dina knän får jobba hårt")
        time.sleep(2)
        print("Plöstlsigt halkar du till och ramlar")
        time.sleep(2)
        print("Du tumlar neråt, det gör ont,")
        time.sleep(2)
        print("Efter vad som känns som en evighet så stannar du entligen")
        time.sleep(2)
        print("Du reser dig upp och kollar dig omkring")
        time.sleep(2)
        print("En lång rak grotta du inte kan se slutet på")
        time.sleep(2)
        print("I perferin ser du rörelser, du vänder dig snabbt om och ser nåting springa mot dig")
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive        # Om du dör så slutar funk köras
    print("Efter du dödat monsteret går du vidare")
    time.sleep(3)  # import time
    print("Du hinner bara gå ett par minuter innan du hör något mullra, du vänder dig om och ser massor stenar rulla mot dig")
    time.sleep(5)
    print("Du lowkey ser ett samband i stenarna, nummrena 13 98 flashar i din hjärna")
    time.sleep(5)  # Låter användaren kolla på nummrerna
    os.system('cls')  # Rensar temrinel
    stensvar = input("vilka var talen?  xx xx")
    time.sleep(2)
    if stensvar == "13 98":
        print("Du fick rätt, du undivker stenarna")
    else:
        print("Du såg inte visionen och blev träffad av en sten")
        playerclass.hp -= 10  # Tar bort liv från gubben
        print(f"Du har nu {playerclass.hp} hp")
    print("Efter stenraset går du vidare")
    time.sleep(5)
    print("Efter ett tag kommer du till en korsning")
    time.sleep(3)
    print("En skylt sitter uppsatt, på den står det")
    time.sleep(3)
    print("Gå vänster om du vill leva")
    if vägescape() == 1:
        print("Du går vänster")
        time.sleep(3)
        print("Grottan börjar snart ljusna och du känner luften bli varmare")
        if vägdecision == 1:  # playern vänder
            print("Du vänder tillbaka")
            time.sleep(3)
            print("Du kommer tillbaka till korsning och går förbi skylten ")
        else:
            print("Du går upp ur grottan")
            return               # Går upp ur grottan och cancela grott äventyret
    else:
        print("Du trotsar skyltens råd och går höger")
    time.sleep(3)
    print("Gången krymper, luften blir kallare. Eko av droppande vatten hörs överallt.")
    time.sleep(2)
    print("Grottan forsätter gå ner snart når vattnet dig upp till midjan")
    time.sleep(2)
    print("Det är svängar överallt, det känns som lybyrint")
    time.sleep(2)
    print("Plötsligt hör du ett isande skrik bakom dig,")
    time.sleep(2)
    afb = input("Vill du, 1 Gå mot ljudet eller 2 gå vidare")
    if afb == "1":
        print("Du vänder dig om och börjar gå")
        time.sleep(2)
        print("Allt ser normalt ut, inget konstigt")
        time.sleep(2)
        print("Kanske inbildade du dig bara")
        time.sleep(2)
        print("Efter ett tag ser du nåt som glimmar på vägen")
        time.sleep(2)
        print("En stor guldtand, intryck i en glipa")
        time.sleep(2)
        print("Den här kan noga vara värd en kosing tänker du")
    else:
        print("Du forsäter gå framåt")
        time.sleep(2)
        print("Rarariarar!")
        time.sleep(2)
        print("Någonting drar dig ner under vattnet")
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
            
    print("Du fick 15 guldmynt")
    playerclass.amoney(15)
    # Öka pengar varibeln
    time.sleep(2)
    print("Du går vidare fast du är trött")
    time.sleep(2)
    print("Långsamt börjar grottan bli torrare")
    time.sleep(3)
    print("Efter en stund märker du att marken blir mjukare, nästan som sand")
    time.sleep(2)
    print("Det luktar fuktigt och mögel, luften känns tung")
    time.sleep(2)
    print("Du hör ett svagt ljud av något som rör sig under sanden")
    time.sleep(2)
    choice = input("Vill du, 1 undersöka ljudet eller 2 fortsätta framåt? ")

    if choice == "1":
        print("Du hukar dig ner och tittar försiktigt")
        time.sleep(2)
        print("Ett par små ögon som iaktar dig från sanden..")
        time.sleep(2)
        print("Du drar fram ditt vapen och förbereder dig för strid!")
        alive = battle(sandworm, playerclass, alive)
        if alive == False:
            return playerclass.alive
        time.sleep(2)
        print("Efter striden andas du ut och fortsätter vidare")
    else:
        print("Du väljer att inte störa det mystiska ljudet och fortsätter framåt")
        time.sleep(2)
        print("Sanden knastrar under dina fötter och gångarna blir smalare")
        print("Plötsligt ser du en stor hiss")
        print("Den ser gammal ut men den kanska funkar")
        hissvar = input("Vill du trycka på hissknappen?")
        if hissvar.len == 2:
            pass

    time.sleep(1)
    print("Plötsligt öppnar grottan upp sig till en enorm sal")
    time.sleep(2)
    print("Takets stalaktiter glittrar av fukt, och små floder rinner kors och tvärs")
    time.sleep(3)
    print("I mitten av salen ser du något som får ditt hjärta att slå snabbare")
    time.sleep(2)
    print("En gigantisk, glittrande drake sover bland högar av guld och skatter")
    time.sleep(2)
    choice2 = input(
        "Vill du, 1 smyga förbi draken eller 2 försöka ta lite skatt? ")

    if choice2 == "1":
        print("Du håller andan och smyger längs väggarna")
        time.sleep(2)
        print("Draken rör inte en muskel och du kommer fram till andra sidan salen")
        print("Du känner dig nöjd men adrenalinet pumpar fortfarande")
    else:
        print("Du tar ett steg mot skatten")
        print("Draken öppnar ett öga och låter ett öronbedövande vrål")
        time.sleep(2)
        # Kalla draken som monster
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        print("Efter en hård strid lämnar du salen med en bit av skatten")
    time.sleep(1)
    print("När du går vidare från salen blir grottan smalare och luften varmare")
    time.sleep(2)
    print("Du börjar se ljus som sipprar in från små sprickor ovanför")
    time.sleep(2)
    print("Det känns som att du närmar dig grottans slut")
    time.sleep(2)
    print("Men plötsligt hör du ett eko av fotsteg bakom dig")
    choice3 = input(
        "Vill du, 1 vända dig om eller 2 fortsätta framåt snabbt? ")
    if choice3 == "1":
        print("Du vänder dig om och ser en grupp skuggfigurer")
        time.sleep(2)
        print("De verkar inte se dig än, kanske kan du smyga undan?")
        stealth_choice = input(
            "Vill du, 1 smyga undan eller 2 konfrontera dem? ")
        if stealth_choice == "1":
            print("Du kryper längs väggarna och lyckas ta dig förbi utan problem")
        else:
            print("Du drar fram ditt vapen och striden börjar")
            # Slåss mot mystical men
            alive = battle(monsterval, playerclass, alive)
            if alive == False:          # Alive ändras i battle func
                return playerclass.alive
    else:
        print("Du rusar framåt och ignorerar fotstegen bakom dig")
        time.sleep(2)
        print("Pulsen dunkar i öronen men du känner ljuset bli starkare för varje steg")

    time.sleep(1)
    print("Slutligen når du grottans mynning")
    time.sleep(2)
    print("Solens ljus träffar ditt ansikte, och du andas de1n friska luften")
    return 


def skogsvägen(alive):
    print("Efter ett tag kommer du fram till en mörk skog.")
    time.sleep(1)
    print("Du kliver in i den mörka skogen. Ljuset bakom dig försvinner nästan direkt när träden sluter sig över dig. Luften blir kylig och stilla. Något prasslar mellan stammarna, men du kan inte se vad. Skuggorna rör sig, och en obehaglig känsla kryper längs ryggen.")
    time.sleep(4)
    if vägdecision() == 1:
        print("Du fegar ut och bestämmer dig för att vandra hem.")
        return 
    else:
        print("Du går djupare in i skogen.")
        time.sleep(2)
        print(
            "Efter ett tag hör du grenarna prassla bakom dig och du vänder dig snabbt om.")
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False: 
            return playerclass.alive         # Alive ändras i battle func
            # global adventuring
            # adventuring = False
            # return
    print("Du fick 15 guldmynt eftersom att du beserade monstret!")
    amoney(15)
    time.sleep(2)
    print("Efter fighten så fortsätter du in i den mörka skogen.")
    time.sleep(3)
    print("Du går sakta och samtdigt njuter av den lugna och stilla miljön.")
    time.sleep(2)
    print("Men helt plötsligt så börjar vinden ta sig och skyn går om till svart.")
    time.sleep(2)
    print("Det föredetta lugnet har nu gått om till en kraftfull storm och träden vajar rejält.")
    time.sleep(2)
    print("Bakifrån dig hörs ett högt knak och vänder dig om för att se ett gigantiskt träd falla mot din riktning")
    time.sleep(3)
    skogsträdfall = int(input("""                            Vill du:
1. Undvika vänster   2. Undvika höger   3. Slå sönder trädet oskadad"""))
    if skogsträdfall == 1:
        print("Du undvek trädet genom att göra en dramatisk rull åt vänster och kom ut oskaddad.")
    elif skogsträdfall == 2:
        print("Du undvek trädet genom att göra en dramatisk rull åt höger och kom ut oskaddad.")
    elif skogsträdfall == 3:
        print("Du försökte stoppa trädet med all din kraft, men blir till slut mosad.")
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        # global alive
        # alive = False
        # global adventuring
        # adventuring = False
        # return
    else:
        print(
            "Du svarade inte korrekt och hinner därför inte reagera på det fallande trädet.")
        time.sleep(3)
        print("Du dog.")
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        # global alive
        # alive = False
        # global adventuring
        # adventuring = False
        # return
    time.sleep(2)


    if vägdecision() == 1:
        print("Du bestämmer dig för att vända tillbaks.")
        return
    else:
        print("Efter katastrofen så fortsätter du djupare in i den mörka skogen medans du vandrar mellan de höga vajande träden, tills du känner att någonting inte riktigt stämmer.")
        time.sleep(4)
        print("2 röda ögon ses blinka mellan träden, och de verkar spana in just dig.")
        time.sleep(2)
        print("På mindre än en sekund löpar monstret och hoppar på dig!")
        time.sleep(2)
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
    if alive == False:        # Alive ändras i battle func
        return playerclass.alive        
        # global adventuring
        # adventuring = False
        # return
        print("Efter ännu en till attack så känner du dig utmattad och fortsätter vandra med hopp om att du snart kommer ut ur denna läskiga skog.")
        time.sleep(4)
        print("Efter ett långt äventyr så ser du ett glimmer från skogens kant och bestämmer dig för att gå denns håll.")
        time.sleep(3)
        print("När du närmrar dig så inser du att det är en liten stuga.")
        time.sleep(2)
    while True:
        try: 
            Stuga_val = int(input("""      Vill du:
            1. Gå in i stugan       2. Strunta i stugan och fortsätta vandra"""))
            if Stuga_val == 1:
                break
                print("Du bestämmer dig för att ta dig in i stugan i hopp om resurser som kan hjälpa dig komma ut ur skogen.")
            elif Stuga_val == 2:
                print()
                break
            else:
                print("Du gav inte ett giltigt svar, svara om.")
        except: 
            print("Du gav inte ett giltigt svar, svara om.")


def abanondedcity(alive):
    print("Efter ett tag kommer du fram till vad du tror är en helt vanlig stad.")
    time.sleep(3)
    print("Men du märker att någonting är fel.")
    time.sleep(2)
    print("Fönstren är krossade, det växer gräs ur asfalten och det är helt tyst förutom vindens brus.")
    time.sleep(4)
    print("Det var nästan som att staden är övergiven.")
    time.sleep(2)
    print("När du funderar på vart du ska ta vägen så ser du en hög skyskrapa som bara kallar ditt namn och du bestämmer dig för att gå dit.")
    time.sleep(4)
    print("Du tar dig genom de övergivna gatorna och efter en lång vandring så kommer du äntligen fram till en otroligt höga byggnaden.")
    time.sleep(5)
    print("Du går in genom porten på den föredetta lyxiga byggnaden i hopp om att hitta resureser.")
    time.sleep(3)
    print("Du kollar runt i den lyxiga entrén som ser oväntande fräsh ut.")
    time.sleep(2)
    print("Allt verkar alldels för avkopplande tills...")
    time.sleep(2)
    monsterval = monsterpullar()
    alive = battle(monsterval, playerclass, alive)
    if alive == False:        # Alive ändras i battle func
        return playerclass.alive 
    if vägdecision() ==1:
        print("Du bestämmer dig för att vända tillbaks.")
        return
    print("Efter fighten så fortsätter du att gå runt i skyskrapan tills du hittar ett par trappor.")
    time.sleep(3)
    while True:
        try:
            trapporupellerner = int(input("""Vill du:
            1. Gå ner för trappan     2. Gå upp för trappan
            """))
            if trapporupellerner == 1:
                time.sleep(1)
                print("Du bestämde dig för att gå upp från trappan.")
                time.sleep(2)
                print("Denna våning verkar vara ett gammalt spelrum med otroligt många olika maskiner och kortspel.")
                time.sleep(3)
                print("Du kollar på alla olika slotmachines och märker att en av dem skapar ett konstigt pling ljud.")
                time.sleep(3)
                print("Du går fram till maskinen och bestämmer dig för att slå lite på den i hopp om att den kanske fortfarande fungerar.")
                time.sleep(3)
                print("Helt plötsligt så börjar den spela ett högt ljud och en lucka öppnar sig.")
                time.sleep(2) 
                print("Ut kom runt 20 mynt, det värkar vara din lyckodag!")
                time.sleep(2)
                print("Du plockar upp mynten och går din väg.")
                amoney(20)
                break
                        
            elif trapporupellerner == 2:
                time.sleep(1)
                print("Du bestämde dig för att gå ner för trappan.")
                time.sleep(2)
                print("Det verkar som att du gått in på föredetta garagevåningen.")
                time.sleep(2)
                print("Det finns lyxiga bilar på din vänster och höger men den som faktiskt väcker ditt intresse är en gammal mint condition Volkswagen Golf.")
                time.sleep(3)
                print("Du går fram till den vackra bilen och bestämmer dig för att se om den fungerar så du bryter dig in via fönsterrutan.")
                time.sleep(3)
                print("Solklart glömmer du ju bort att det behövs nycklar så du går ut ur bilen i misstro fast någonting glimmade till i baksätet och bestämmer dig för att tar ännu en tit in i bilen.")
                time.sleep(5)
                print("Det visade sig vara ett golfsett.")
                time.sleep(1)
                while True:
                    try:
                        time.sleep(2)
                        Tauppbackseatweapon = int(input(f"""Vill du plocka upp en golfklubba och byta ut den mot ditt nuvarande vapnet {Weapon.name}?
                        1. Ja     2. Nej"""))
                        if Tauppbackseatweapon == 1:
                            print(f"Du bytte ut {Weapon.name} mot en golfklubba")
                            Vapen = Weapon("Golfklubba")
                            playerclass.weapon = Vapen
                            break
                        elif Tauppbackseatweapon == 2:
                            print(f"Du behöll {Weapon.name} som ditt vapen.")
                            break
                        else:
                            print("Du gav inte ett giltigt svar, svara om.")
                    except:
                        print("Du gav inte ett giltigt svar, svara om.")
                            
                print("Efteråt återvände du tillbaks till stadens gator.")
                break
                        
            else:
                print("Du gav inte ett giltigt svar, svara om.")
        except:
            print("Du gav inte ett giltigt svar, svara om.")
time.sleep(2)
print("Efter ett långt äventyr så blev du klar med att undersöka skyskrapan och du kan äntligen gå hem.")
time.sleep(3)
print("I det trista väderet går du över de sprukna gatorna.")
time.sleep(2)
print("Det är knäpptyst i staden förutom vindens sus.")
time.sleep(2)
print("Men i tystnaden så hörs ett skräckinjagande vrål.")
time.sleep(2)
while True:
    try:
        museumfortsättaellerundersöka = int(input("""Vill du undersöka vrålet eller vill du fortsätta ut ur staden?
        1. Undersöka     2. Fortsätta"""))
        if museumfortsättaellerundersöka == 1:
            time.sleep(1)
            print("Du bestämmer dig för att undersöka vrålet och ändrar din gåriktning.")
            time.sleep(2)
            print("Vrålet forsätter och blir högre och högre för varje steg du tar.")
            time.sleep(2)
            print("Du börjar närma dig vrålets källa och kan snart se var detta skrämmande ljud kommer ifrån.")
            time.sleep(3)
            print("Framför dig syns en otroligt stor och urgammal byggnad, det verkar vara ett sorts museum.")
            time.sleep(2)
            if vägdecision() ==1:
                print("Du bestämmer dig för att vända tillbaks.")
                return
            time.sleep(2)
            print("Vrålet har ännu än inte slutat och du bestämmer dig för att går in och äntligen få reda på vad som skapar oljudet")
            time.sleep(3)
            print("Du öppnar lätt dörren och tar en liten titt in i museets entré.")
            time.sleep(2)
            print("Det chockande rent eftersom att det troligen inte varit någon här på flera decennier.")
            time.sleep(3)
            print("Du går in genom dörren och sekunden som porten stängs bakom dig så slutar plötsligt vrålandet och det blir helt knäpptyst.")
            time.sleep(3)
            print("Du går ")
            break
        elif museumfortsättaellerundersöka ==2:
            time.sleep(1)
            print("Du bestämmer dig för att strunta i vrålet och fortsätter istället åt samma håll som du först tänkte gå.")
            break
        else:
            print("Du gav inte ett giltigt svar, svara om.")
    except:
        print("Du gav inte ett giltigt svar, svara om.")
def biblloktekt():
    while True:
            bok_val = int(input("""        Var vill du gå?
                        1. Monster boks hyllan        2. Natur boks hyllan      3. Den vise mannen
                                                4. Gå tillbaka
                        """))
            

            if bok_val == 1:
                        monster_val = int(input("""    Vilket monster skulle du vilja läsa om?
                                        1. Skeleton     2. Goblin       3. Goon        4. Bandit
                                                        5. Troll        6. Varulv 
                                                                7. Lämna
                        """))
                        try:
                            if monster_val == 1:
                                    slowtype("""En forntida krigare vars själ aldrig fann ro. Benen är sammanbundna av förbannad vilja,\n
och i ögonhålorna lyser ett svagt blått sken. Skeletons vaknar där strider en gång rasade,
alltid redo att fortsätta ett krig som för länge sedan tagit slut.""", 0.05)
                            elif monster_val == 2:
                                    slowtype("""Små, gröna och evigt irriterande. Goblins trivs i skuggorna där de skrattar åt sina egna dumma skämt.\n
Deras svaga kroppar gör dem fega, men deras hastighet och list gör dem farliga i grupp.\n
En ensam goblin är ett problem – en flock är en katastrof.
""", 0.05)
                            elif monster_val == 3:
                                    slowtype(""" En trasig själ med en kropp som verkar ihopslängd av kaos självt. Goons är förvirrade, oberäkneliga och farliga.\n
De förstår inte rädsla, inte smärta och ibland inte ens att de är i en strid. Deras slumpslag kan vara både värdelösa – eller dödliga.
""", 0.05)
                            elif monster_val == 4:
                                    slowtype("""En före detta människa som valde mörka vägar.\n
Deras snabbhet, vassa knivar och ännu vassare instinkter gör dem dödliga plågoandar längs vägarna.\n
Banditer attackerar inte för nöje – utan för överlevnad.
""", 0.05)
                            elif monster_val == 5:
                                    slowtype(""" Troll föds ur jordens djup, formade av lera och sten.\n
De är långsamma i både huvud och kropp, men när de slår – skälver världen.\n
Många äventyrare föraktar troll, men få vet att deras hjärtan slår med sorg efter förlorade skogar.
                                    """, 0.05)
                            elif monster_val == 6:
                                    slowtype(""" En människa förbannad av månen. När skymningen faller förlorar de förståndet och förvandlas till en snabb, brutal predator.\n
Deras ylande ekar genom nattens skogar och deras klor lämnar djupa ärr i både trä och kött.
""", 0.05)
                            elif monster_val == 7:
                                break
                            else:
                                print("Skriv ett av de 7 nummer")
                        except:
                            print("Skriv om skriv rätt")

            elif bok_val == 2:
                        try:
                            natur_val = int(input("""       Vilken natur vill du läsa om?
                                        1. Grottvägen       2. Skogsvägen       3. Abanonded City
                                                            4. Lämna
                            """))
                            if natur_val == 1:
                                slowtype("""Grottvägen är en labyrint av trånga tunnlar och fuktiga gångar som har formats under tusentals år av rinnande vatten och erosion.\n
Droppstenar och stalaktiter hänger hotfullt från taket, och marken är halt och stenig.\n
Den här platsen har alltid varit en passage mellan världens yttre landskap och de djupare, hemliga underjordiska gångarna – fylld av mystik och faror.
""", 0.05)
                            elif natur_val == 2:
                                slowtype("""Skogsvägen slingrar sig genom täta skogar, där träden sträcker sig högt mot himlen och dimman ofta ligger tät mellan stammarna.\n
Marken är mjuk av mossa och fallna löv, och vinden får trädens grenar att knaka hotfullt.\n
Skogsvägen har funnits i århundraden som en naturlig passage för resande och äventyrare, men dess orörda djup rymmer både skönhet och fara\n
""", 0.05)
                            elif natur_val == 3:
                                slowtype(f"""Den övergivna staden är en ruin från en svunnen civilisation. \n
Krossade byggnader, trasiga gator och murar som rasat under tidens gång ger staden ett spöklikt utseende.\n
Staden byggdes en gång som ett centrum för handel och magi, men drabbades av okända katastrofer och övergavs.\n
Nu ekar tystnaden mellan ruinerna, och platsen bär på historiens mysterier och glömda hemligheter.
""", 0.05)
                            elif natur_val == 4:
                                break
                            else:
                                print("Skriv ett av de 4 nummer")
                        except:
                            print("Skriv om och skriv rätt")
                    
            elif bok_val == 3:
                    if playerclass.hybris == True:                         #chekar om playern har hybris
                        slowtype("The old man is not here anymore, wonder why...", 0.1)
                    else:
                            slowtype("Hello there young man", 0.15) 
                            slowtype("I'am the wise man of the village", 0.1)
                            gusval = input("Do you want to hear about my life? Ja / Nej")
                            gusval = gusval.upper()
                            if gusval == "NEJ":
                                slowtype("All these young men", 0.1)
                                time.sleep(0.5)
                                slowtype("How many have walked past me",0.1)
                                time.sleep(0.5)
                                slowtype("To never return ",0.1)
                                time.sleep(0.5)
                                slowtype("I have seen them all but not even Leonard Euler could have counted them ",0.1)
                                time.sleep(0.5)
                                slowtype("Goodbye", 0.1)
                                playerclass.hybris = True     #Sätter playern som hybris
                                
                            else:
                                slowtype("In my youth i was a adeventurer", 0.15)
                                time.sleep(0.5)
                                slowtype("I walked through caves that were so dark", 0.15)
                                time.sleep(0.5)
                                slowtype("Even god didn't know what lived down there", 0.15)
                                time.sleep(0.5)
                                slowtype("I walked in forests with tress so tall", 0.15)
                                time.sleep(0.5)
                                slowtype("Even the birds didnt know were they ended", 0.15)
                                time.sleep(0.5)
                                slowtype("And i walked through cities that were soo haunted", 0.15)
                                time.sleep(0.5)
                                slowtype("Even the devil had stoped counting the lost souls", 0.15)
                                time.sleep(0.5)
                                slowtype("After all my experinces abroad i returned home with fainted heart", 0.15)
                                time.sleep(0.5)
                                slowtype("I settled down and became the old man you see before you", 0.15)
                                time.sleep(2)
                                slowtype("But now on the sunset of my life", 0.12)
                                time.sleep(0.5)
                                slowtype("I wished i walked out there one more time", 0.1)
                                time.sleep(2)
                                slowtype("Becuase there is still something out there", 0.1)
                                time.sleep(0.5)
                                slowtype("A creature i only felt the aura from", 0.1)
                                time.sleep(0.5)
                                slowtype("Only when that king of darkness is erased can the world's darkness disappaear", 0.1)
                                time.sleep(0.5)
                                slowtype("Now son, i wish that you get out there deafeat him",0.1)
                                time.sleep(2)
                                slowtype("Only then can i die happy", 0.1)
                    break
                        
                    
            elif bok_val == 4: 
                        break
            else:
                        slowtype("Skriv ett av de 4 nummer", 0.2)
    return playerclass.hybris       #Skickar tillbaka om playern har hybris eller inte


        
            


def main(alive):
    while alive == True:
        time.sleep(1)
        print(f"""          Sweelept
        1. Äventyr       2. Markanden       3. Bibloteket
    
                    4. Stats allocation  5. Casino
            """)
        time.sleep(1)
        Platsval = input("Vad vill du välja? ")
        if Platsval == "1":
            print("Du har valt att äventyra!")
            time.sleep(1)
            print("Du traskar ut ur staden och snart uppenbarare sig en skog där vägen försvinner till tre stigar")
            time.sleep(1)

            plats = korsningen()
            if plats == "ja":
                adventuring = False
                break      # Slutar while loopen
            elif plats == 1:
                alive = grottvägen(alive)
            elif plats == 2:
                alive =skogsvägen(alive)
            elif plats == 3:
                alive = abanondedcity(alive)
            else:
                 print("error i main")
            if alive == False:
                print("fnaj")

        elif Platsval == "2":
            print("Du har valt att gå till markanden")
            Markanden()
        elif Platsval == "3":
            print("Du har valt att gå till biblloktekt")
            playerclass.hybris = biblloktekt()   #Sparar om playern har hybris eller inte
            

        elif Platsval == "4":
            print("hej")
            # Stats allocation och stat check
        elif Platsval == "5":
            casion()
        else:
            pass

main(alive)
# li = []


# for i in range(10):
#     m = Monster("goblin", 10, 15, 22)
#     li.append(m)


# healthpotion = Items("Health_potion", 10, 0, 1)
# strengthpotion = Items("strength_potion", 0, 10, 1)


# svärd = Weapon("Snopp", 25, 1, 1)

# print(svärd)
