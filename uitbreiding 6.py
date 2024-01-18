import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3

getal1 = random.randint(10, 25)
getal2 = random.randint(-5, 75)
totaal = getal1 + getal2
sleutel = False
rubee = 0

zombie_attack = 1
zombie_defense = 0
zombie_health = 2

monster_attack = 2
monster_defense = 0
monster_health = 3

dubbel_steen_1 = random.randint(1,6)
dubbel_steen_2 = random.randint(1,6)

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)
# ===[kamer 7] ===#

print('hier krijg je een rubee en hiermee kan je wapen kopen als je dat wilt')
kant_kiezen = input('wil je rechts of rechtdoot gaan')
rubee += 1

if kant_kiezen == 'rechtdoor':
    # === [kamer 2] === #
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    print(f'Daarboven zie je een som staan {getal1} + {getal2}=?')
    antwoord = int(input('Wat toets je in?'))

    if antwoord == totaal:
        print('Het standbeeld laat de sleutel vallen en je pakt het op.')
        sleutel = True
    else:
        print('Er gebeurt niets....')

    print('Je ziet een deur achter het standbeeld.')
    print('')
    time.sleep(1)
    keuze_kamer2 = input('Wil je naar kamer 6 of kamer 3 gaan? (Typ "6" of "8"): ')
    # === kamer 6 === #
    if keuze_kamer2 == '6':
        print('Je opent de deur naar kamer 6.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage = (zombie_attack - player_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        else:
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

            player_hit_damage = (player_attack - zombie_defense)
            player_attack_amount = math.ceil(zombie_health / player_hit_damage)

            if player_attack_amount < zombie_attack_amount:
                print(f'In {player_attack_amount} rondes versla je de zombie.')
                player_health -= player_attack_amount * zombie_hit_damage
                print(f'Je health is nu {player_health}.')
            else:
                print('Helaas is de zombie te sterk voor je.')
                print('Game over.')
                exit()
        print('')
        time.sleep(1)

print('')

print('je bent nu bij kamer 8 hier is een gok machine waarmee je ruppees kan verdubbelen')
print('als je totaal dubbelsteen groter dan 7 dan verdubbelt je ruppees')
print('als je totaal dubbelsteen kleiner is dan 7 dan gaat er een punt af van je health')
print('als je totaal dubbelsteen gelijk is aan 7 dan verdubbelt je ruppees en gaat en een punt af van je health')
print('wil je spelen type een ja')
time.sleep(1)

gok_machine = input('wil je gokken')
if gok_machine == 'ja':
    print('het eind resultaat van je gok speel is ')
    totaal_dubbel_steen = dubbel_steen_1 + dubbel_steen_2
    if totaal_dubbel_steen > 7:
        rubee *= rubee
        print(f'gefeliciteerd je ruppees zijn verdubbelt je hebt nu {rubee} ruppees ')
    elif totaal_dubbel_steen < 7:
        player_health -= 1
        print(f'helaas is er een punt van je health afgehaald je nieuwe health is {player_health}')
        if player_health < 0:
            print('game over')
            exit()
    else:
        rubee *= rubee
        player_health -=1
        print('helaas is er een punt van je health weggehaald maar je ruppees zijn verdubbelt')
        print('')
    print(f'je hebt {totaal_dubbel_steen}')
# === [kamer 3] === #
print('hier in kamer 3 kan je zwaard of schild kopen')
wapen_kopen = input('wil je (zwaard) of (schild) of (niks) kopen')
if wapen_kopen == 'zwaard':
    player_attack += 2
    rubee -= 1
elif wapen_kopen == 'schild':
    player_defense += 1
    rubee -= 1
else:
    print('je hebt niks gekocht')
    wapen_kopen = False

if wapen_kopen:
    print('Je duwt de deur open en stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {wapen_kopen}.')
    print(f'Je pakt het {wapen_kopen} op en houdt het bij je.')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

# === [kamer 4] === #

monster_hit_damage = (monster_attack - player_defense)
if monster_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de monster, hij kan je geen schade doen.')
else:
    monster_attack_amount = math.ceil(player_health / monster_hit_damage)

    player_hit_damage = (player_attack - monster_defense)
    player_attack_amount = math.ceil(monster_health / player_hit_damage)

    if player_attack_amount < monster_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de monster.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de monster te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een monster tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if sleutel:
    print('Je hebt de sleutel van de schatkist. Gefeliciteerd, je hebt gewonnen!')
else:
    print('Je hebt geen sleutel. Game over.')
