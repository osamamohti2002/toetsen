import time
import math
import random

def zombie_gevecht(zombie, player_attack, player_defense, player_health, zombie_attack, zombie_defense, zombie_health):
    print(f'Je loopt tegen een {zombie} aan.')
    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            player_health = player_health - (player_attack_amount * zombie_hit_damage)
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    time.sleep(1)
    return player_health


player_attack = 1
player_defense = 0
player_health = 3
rupee = 0
sleutel = False
schatkist = 'sleutel'

kamer9 = False

# === [kamer 1] === #
print("=== [kamer 1] ===")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(2)

# === [kamer 7] === #
print("=== [kamer 7] ===")
kans_voor_rupee = random.randint(1, 10)
if kans_voor_rupee == 2:
    rupee += 1
    print(f"Je krijgt nu {rupee} rupee zodat je straks je eigen wapens kan kopen.")
else:
    print("Je vindt niets opvallends in deze kamer.")
print('')
time.sleep(2)

kamer7_keuze = int(input('wil je naar kamer 8 of kamer 2? '))
if kamer7_keuze == 2:
    # === [kamer 2] === #
    print("=== [kamer 2] ===")
    eerste_getal = random.randint(10, 25)
    tweede_getal = random.randint(-5, 75)
    juiste_antwoord = eerste_getal + tweede_getal

    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print(f'Daarboven zie je een som staan {eerste_getal} + {tweede_getal}')
    antwoord = int(input('Wat toest je in? '))
    if antwoord == juiste_antwoord:
        rupee += 1
        print("Juist je hebt goed gerekend")
        print(f"Hier bij krijg je {rupee} rupee.")
    else:
        print("helaas dat is niet de juiste antwoord")
    print('Je zie een deur achter het standbeeld.')

    kamer2_keuze = int(input('wil je naar kamer 8 of kamer 6? '))
    if kamer2_keuze == 6:
        # === [kamer 6] === #
        print("=== [kamer 6] === ")
        zombie = 'zombie'
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2

        zombie_gevecht(zombie, player_attack, player_defense, player_health, zombie_attack, zombie_defense, zombie_health)
        kamer6_keuze = int(input('wil je naar kamer 3 of kamer 8? '))

if kamer7_keuze == 8 or kamer2_keuze == 8 or kamer6_keuze == 8:
    # === [kamer 8] === #
    print("=== [kamer 8] ===")

    eerste_dubbel_steen = random.randint(1, 7)
    tweede_dubbel_steen = random.randint(1, 7)
    uitkomst = eerste_dubbel_steen + tweede_dubbel_steen
    gokmachine = input("Er is een gokmachine wil je het gebruiken (ja/nee)? ")
    if gokmachine == 'ja':
        print(uitkomst)
        if uitkomst > 7:
            rupee += 1
            print(f" JE hebt een rupee gewonnen, je huidige saldo is {rupee}")
        elif uitkomst < 7:
            player_health -= 1
            print(f"Helaas je hebt een Health verloren, je huidige health is {player_health}")
            if player_health == 0:
                print("Game over")
                exit()
        elif uitkomst == 7:
            rupee += 1
            player_health -= 1
            print(f"Je hebt toch een rupee gewonnen {rupee} maar toch heb je een health verloren {player_health}")
    else:
        print("JE mag door")
        print("")
        time.sleep(2)

    kamer8_keuze = int(input("Wlke kamer wil je heen gaan (3/9)? "))
    if kamer8_keuze == 9:
        print("Kamer9")
        # === [kamer 9] === #
        print("JE komt naar kamer waarbij hulp middelen zijn")
        hulp_middel = random.choice([player_defense, player_health])

        if hulp_middel == player_defense:
            player_defense += 1
            print(f"Je hebt defense gekregen je huidige defense is {player_defense}")
        else:
            player_health += 2
            print(f"Je hebt een health gekregen en je huidige health is {player_health}")
            kamer9 = True
        print("")
        time.sleep(2)

    # if kamer9 != False or kamer8_keuze == 3 or kamer6_keuze == 3:
# === [kamer 3] === #
print("Welkom in kamer3 ")
print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'Je huidige saldo is {rupee} rupee')
if rupee >= 3 or rupee >= 2:
    wapens_keuze = input("Wil de wapens (los) kopen of (alles) of (niks)? ")
    if wapens_keuze == "alles":
        player_attack += 2
        player_defense += 1
        sleutel = True
        rupee -= 3
        wapens_keuze = 'schild en zwaard'
        print(f"JE hebt alle wapens en sleutel gekocht en je huidige slado is {rupee} rupee ")
    elif wapens_keuze == "los":
        wapens_keuze = input("Welke wapen wil je kiezen (zwaard/schild) of (sleutel) of (niks)? ")
        if wapens_keuze == 'zwaard':
            player_attack += 2
            rupee -= 1
        elif wapens_keuze == 'schild':
            player_defense += 1
            rupee -= 1
        elif wapens_keuze == "sleutel":
            sleutel = True
        print(f"Je hebt een {wapens_keuze} gekocht! en je huidige saldo is {rupee} rupee")
elif rupee == 1:
    wapens_keuze = input("Welke wapen wil je kiezen (zwaard/schild) of sleutel? ")
    if wapens_keuze == 'zwaard':
        player_attack += 2
        rupee -= 1
    elif wapens_keuze == 'schild':
        player_defense += 1
        rupee -= 1
    elif wapens_keuze == 'sleutel':
        sleutel = True
    print(f"Je hebt een {wapens_keuze} gekocht! en je huidige saldo is {rupee} rupee")
else:
    print("JE hebt niks gekocht!")
print('Op naar de volgende deur.')
print('')
time.sleep(2)

# === [kamer 4] === #
print("=== [kamer 4] ===")
zombie = 'monster'
zombie_attack = 2
zombie_defense = 0
zombie_health = 3

zombie_gevecht(zombie, player_attack, player_defense, player_health, zombie_attack, zombie_defense, zombie_health)

# === [kamer 5] === #
print("=== [kamer 5] ===")
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if sleutel:
    print("Je kan de schatkist open maken, je hebt gewonnen")
else:
    print("Je kan de schatkist niet open maken. Je verliest.")
    print("Game over")
    exit()

