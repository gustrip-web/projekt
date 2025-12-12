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
                Weapon("Smörkniv", 1.25, 0.25, 2),
                Weapon("Yxa", 4, 0.05, 1.5),
                Weapon("Knogjärn", 2, 0.25, 1.25)]

# Items
Item_list1 = [Item("Small_Health_Potion", 15, 0),
              Item("Medium_Helth_Potion", 30, 1),
              Item("Big_Health_Potion", 60, 1),
              Item("Damage_boost", 0, 1.5)]

# Monster
monster_list1 = [Monster("Skeleton", 40, 20, 1),
                 Monster("Goblin", 75, 10, 1),
                 Monster("Goon", 35, 5, 1),
                 Monster("Bandit", 50, 13, 1)]

monster_list2 = [Monster("Demon", 175, 28, 1),
                 Monster("Troll", 250, 18, 1),
                 Monster("Vandrande Själ", 100, 35, 1),
                 Monster("Varulv", 200, 23, 1)]

monster_list3 = [Monter("Jätte", 400, 35, 1),
                 Monster("Drake", 300, 45, 1),
                 Monster("Skuggriddare", 275, 50, 1),
                 Monster("Golem", 450, 20, 1)]

sandworm = Monster("Sandworm", 124, 24, 1)
if Characterclass.lvl < 5:
    monsterpullar = monster_list1
elif Characterclass.lvl >= 5 and Characterclass.lvl < 10:
    monsterpullar = monster_list2
else:
    monsterpullar = monster_list3

# Gameplay
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
        elif val == "0":
            continue
        elif val == "2":
            playerclass = magi
            break
        elif val == "3":
            playerclass = tank
            break
        elif val == "4":
            playerclass = gambler
            break
        else:
            print("skriv ett tal")
    else:
        print("skriv ett tal")
playername = input("Vad ska din karaktär heta? ")

alive = True
adventuring = False
Shopping = False
Reading = False

Player_weapon = Hands


def korsningen():
    plats = rand.randint(1, 2, 3)  # Bestämmer vilken väg som du kommer till
    väghem = rand.randint(1, 2)  # Slumpar om du kan komma hem
    if väghem == 1:  # Väg hem finns
        print("Du kommer till en skog där stigen blir till en väg och till två stigar")
        vägval = input(
            "Vilken stig väljer du? 1 = Vägen, 2 = Stig nr1, 3 = Steg nr2")
        if vägval == "1":
            gårhem = "ja"
            return        # returnera värdern som player fått under äventyret
        else:
            print(f"Du går {vägval}")
    else:
        print("Du kommer till en skog där stigen blir till tre stigar")
        vägval = input(
            "Vilken stig väljer du? 1 = Stig , 2 = Stig nr1, 3 = Steg nr2")
        print(f"Du går {vägval}")
    return plats, gårhem


def vägdecision():  # Väg val på de olika vägarna
    vägval3 = input("Vill du vända tillbaka? ja eller nej")
    if len(vägval3) == 2:
        vägsvar3 = 1      # Player vill vända tillbaka
    else:
        vägsvar = 2  # Vill forsätta
    return vägsvar


def vägescape():  # Väg val på de olika vägarna
    vägval4 = input("Vill du gå vänster eller höger?")
    if len(vägval3) == 6:
        vägsvar3 = 1      # Player vill gå vänstern
    else:
        vägsvar = 2  # Vill gå höger
    return vägsvar


def monsterpullar():
    monsterval = rand.choice(monster_list1)
    print("Du ser monstret {monsterval.name}")
    return monsterval


def battle(monsterpullar, playerclass, alive):
    while playerclass.hp > 0 and monsterpullar.hp > 0:

        battlec = input(f"""Vad vill du göra?   Du har {playerclass.hp} hp,
        Monstrets har {monsterpullar.hp} hp
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

            monsterpullar.hp -= dmg
            print(
                f"Du skadade {monsterpullar.name} med {dmg}! Nu har {monsterpullar.name} {monsterpullar.hp} hp kvar.")
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

        if monsterpullar.hp <= 0:
            print("Du dödade monstret!")
            reward = monsterpullar.exp_reward()
            playerclass.add_exp(reward)
            return
        print(f"{monsterpullar.name} attackerar dig och gör {monsterpullar.dmg} skada!")
        playerclass.hp -= monsterpullar.dmg
        print(f"Nu har du {playerclass.hp}hp kvar")

        if playerclass.hp <= 0:
            print("Du blev besegrad av monstret!")
            playerclass.alive == False
            return playerclass


def grottvägen():
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
            
    print("Du fick 20 guldmynt")
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
    print("Solens ljus träffar ditt ansikte, och du andas den friska luften")
    return 


def skogsvägen():
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
    print("Du fick 20 guldmynt eftersom att du beserade monstret!")
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
    Stuga_val = int(input("""      Vill du:
     1. Gå in i stugan       2. Strunta i stugan och fortsätta vandra"""))
    if Stuga_val == 1:
        print("Du bestämmer dig för att ta dig in i stugan i hopp om resurser som kan hjälpa dig komma ut ur skogen.")
    elif Stuga_val == 2:
        print()
    else:
        print("Du gav inte ett giltigt svar, svara om.")


def abanondedcity():
    pass
    print("Efter ett tag kommer du fram till vad du tror är en helt vanlig stad.")
    time.sleep(3)
    print("Men du märker att någonting är fel.")
    time.sleep(2)
    print("Fönstren är krossade, det växer gräs ur asfalten och det är helt tyst förutom vindens brus.")
    time.sleep(3)
    print("Det var nästan som att staden är övergiven.")
    time.sleep(2)
    print("När du funderar på vart du ska ta vägen så ser du en hög skyskrapa som bara kallar ditt namn. Men sekunden du tänkte ändra din gåriktning så ser du en otroligt fint historiemuseum i din ögonvrå.")
    
def skyskrapan():


def museum():

    while true:
        try:
            abandonedcitywalkchoice = int(input("""Till vilken byggnad vill du gå till?:
            1. Skyskrapan        2. Museumet """))
            if abandonedcitywalkchoice == 1:
                skyskrapan()
                break
            elif abandonedcitywalkchoice == 2:
                museum()
                break
            else:
                print("välj ett av valen")
        except: 
            print("Du skrev inget giltigt svar, svara igen.")

        
            


def main(alive):
    while alive == True:
        print(f"""          Sweelept
        1. Äventyr       2. Markanden       3. Bibloteket

        {lvl}       4. Stats allocation
            
            """)
        Platsval = input("Var vill du gå")
        if Platsval == "1":
            print("Du har valt att äventyra")
            print("Du traskar ut ur staden ")
            print("Snart uppenbarare sig en skog där vägen försvinner till tre stigar")
            input("Vilken väg vill du gå?")
            plats, gårhem = korsningen()
            if gårhem == "ja":
                adventuring = False
                break      # Slutar while loopen
            if plats == 1:
                alive = grottvägen(alive)
            elif plats == 2:
                alive =skogsvägen(alive)
            elif plats == 3:
                alive = abanondedcity(alive)
            if alive == false:
                break

        elif Platsval == "2":
            print("Du har valt att gå till markanden")

        elif Platsval == "3":
            print("Du har valt att gå till biblloktekt")
            bok_val = input("""        Vilken bok skulle du vilja läsa?
                        1. Monster boken        2. Natur boken      3. Den vise mannen
                        """)
            while true:
                if bok_val == "1":
                    monster_val = input("""    Vilket monster skulle du vilja läsa om?
                                    1. Skeleton     2. Goblin       3. Goon        4. Bandit
                                                    5. Troll        6. Varulv 
                                                            q. Lämna
                    """)
                    if monster_val == "1":
                        print("""En forntida krigare vars själ aldrig fann ro. Benen är sammanbundna av förbannad vilja,
                        och i ögonhålorna lyser ett svagt blått sken. Skeletons vaknar där strider en gång rasade,
                        alltid redo att fortsätta ett krig som för länge sedan tagit slut.""")
                    elif monster_val == "2":
                        print("""Små, gröna och evigt irriterande. Goblins trivs i skuggorna där de skrattar åt sina egna dumma skämt.
                        Deras svaga kroppar gör dem fega, men deras hastighet och list gör dem farliga i grupp.
                        En ensam goblin är ett problem – en flock är en katastrof.
                        """)
                    elif monster_val == "3":
                        print(""" En trasig själ med en kropp som verkar ihopslängd av kaos självt. Goons är förvirrade, oberäkneliga och farliga.
                        De förstår inte rädsla, inte smärta och ibland inte ens att de är i en strid. Deras slumpslag kan vara både värdelösa – eller dödliga.
                        """)
                    elif monster_val == "4":
                        print("""En före detta människa som valde mörka vägar.
                        Deras snabbhet, vassa knivar och ännu vassare instinkter gör dem dödliga plågoandar längs vägarna.
                        Banditer attackerar inte för nöje – utan för överlevnad.
                        """)
                    elif monster_val == "5":
                        print(""" Troll föds ur jordens djup, formade av lera och sten.
                        De är långsamma i både huvud och kropp, men när de slår – skälver världen.
                        Många äventyrare föraktar troll, men få vet att deras hjärtan slår med sorg efter förlorade skogar.
                        """)
                    elif monster_val == "6":
                        print(""" En människa förbannad av månen. När skymningen faller förlorar de förståndet och förvandlas till en snabb, brutal predator.
                        Deras ylande ekar genom nattens skogar och deras klor lämnar djupa ärr i både trä och kött.
                        """)
                    else:
                        pass
                    continue
            elif bok_val == "2":
                natur_val = input("""       Vilken natur vill du läsa om?
                                1. Grottvägen       2 .Skogsvägen       3. Abanonded City
                """)
                if natur_val == "1":
                    print("""Grottvägen är en labyrint av trånga tunnlar och fuktiga gångar som har formats under tusentals år av rinnande vatten och erosion.
                    Droppstenar och stalaktiter hänger hotfullt från taket, och marken är halt och stenig.
                    Den här platsen har alltid varit en passage mellan världens yttre landskap och de djupare, hemliga underjordiska gångarna – fylld av mystik och faror.
                    """)
                elif natur_val == "2":
                    print("""Skogsvägen slingrar sig genom täta skogar, där träden sträcker sig högt mot himlen och dimman ofta ligger tät mellan stammarna.
                    Marken är mjuk av mossa och fallna löv, och vinden får trädens grenar att knaka hotfullt.
                    Skogsvägen har funnits i århundraden som en naturlig passage för resande och äventyrare, men dess orörda djup rymmer både skönhet och fara
                    """)
                elif natur_val == "3":
                    print("""Den övergivna staden är en ruin från en svunnen civilisation.
                    Krossade byggnader, trasiga gator och murar som rasat under tidens gång ger staden ett spöklikt utseende.
                    Staden byggdes en gång som ett centrum för handel och magi, men drabbades av okända katastrofer och övergavs.
                    Nu ekar tystnaden mellan ruinerna, och platsen bär på historiens mysterier och glömda hemligheter.
                    """)
                else:
                    pass
                continue
            elif bok_val == "3":
                pass

        elif Platsval == "4":
            print("hej")
            # Stats allocation och stat check
        else:
            print("Skriv ett nummer yaniii")


# li = []


# for i in range(10):
#     m = Monster("goblin", 10, 15, 22)
#     li.append(m)


# healthpotion = Items("Health_potion", 10, 0, 1)
# strengthpotion = Items("strength_potion", 0, 10, 1)


# svärd = Weapon("Snopp", 25, 1, 1)

# print(svärd)
