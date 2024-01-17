import random
import math


# player_defens = 0
# player_attack = 0
# getal1 = random.randint(10,25)
# getal2= random.randint(-5,75)
# totaal = (getal1 + getal2)
#
# print(getal1)
# print(getal2)
# print(totaal)
#
# wapens = ['schild', 'zwaard']
#
# kiezen = random.choice(wapens)
# print(kiezen)
#
# if kiezen == 'schild':
#     player_defens += 1
# else:
#     player_defens += 2
#
# print(player_defens)
# print(player_attack)

player_attack = 1
player_defense = 0
player_health = 3


zombie_attack = 1
zombie_defense = 0
zombie_health = 2

player_hit_damage = (player_attack - zombie_defense)

zombie_hit_damage = (zombie_attack - player_defense)
player_attack_amount = math.ceil(zombie_health / player_hit_damage)

new_helth = player_attack_amount * zombie_hit_damage
print(new_helth)
print(zombie_hit_damage)