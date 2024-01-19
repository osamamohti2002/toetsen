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

kamer1 = False
kamer2 = False
kamer3 = False
kamer4 = False
kamer5 = False
kamer6 = False
kamer7 = False
kamer8 = False
kamer9 = False
kamer10 = False
kamer11 = False
kamer12 = False
kamer13 = False
kamer14 = False
kamer15 = False

player_attack = 1
player_defense = 0
player_health = 3
rupee = 0
sleutel = False
schatkist = 'sleutel'

# === [kamer 1] === #
print("=== [kamer 1] ===")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(2)

# === [kamer 7] === #
print("=== [kamer 7] ===")
kans_voor_rupee = random.randint(1, 2)
if kans_voor_rupee == 2:
    rupee += 1
    print(f"Je krijgt nu {rupee} rupee zodat je straks je eigen wapens kan kopen.")
else:
    print("Je vindt niets opvallends in deze kamer.")
print('')
time.sleep(2)

kamer_keuze = int(input('wil je naar kamer 8 of kamer 2? '))
if kamer_keuze == 2:
    kamer2 = True
    kamer_keuze = int(input('wil je naar kamer 8 of 6? '))
    if kamer_keuze == 6:
        kamer6 = True
        

