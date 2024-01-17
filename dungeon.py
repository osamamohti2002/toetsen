import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
getal1 = random.randint(10,25)
getal2= random.randint(-5,75)
totaal = (getal1 + getal2)
sleutel = False
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {getal1} + {getal2}=?')
antwoord = int(input('Wat toest je in?'))

if antwoord == totaal:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    sleutel = True
else:
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)

# === [kamer 3] === #
item = ['schild', 'zwaard']
wapen = random.choice(item)
if wapen == 'schild':
    player_defense += 1
else:
    player_attack += 2

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {wapen}.')
print(f'Je pakt het {wapen} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {wapen} loop je de kamer binnen.')
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

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if sleutel:
    print('je hebt de sleutel van de schatkist Gefeliciteerd je hebt gewonnen')
else:
    print('je hebt geen sleutel Game over')