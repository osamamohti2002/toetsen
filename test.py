if rupee >= 2:
    wapens_keuze = input("Je kan nu je eigen wapen keizen antwoord met (schild en zwaard) of (niks): ")
    if wapens_keuze  == "schild en zwaard":
        player_defense += 1
        player_attack += 2
        rupee -= 2
        print(f"Je hebt twee wapens gekocht. en je huidige slado is {rupee}")
elif rupee == 1:
    wapens_keuze = input("JE mag een wapen keizen schild/zwaard of niks : ")
    if wapens_keuze == 'schild':
        player_defense += 1
        rupee -= 1
        print(f"Je hebt een schild gekocht. en je huidige saldo {rupee}")
    elif wapens_keuze ==  'zwaard':
        player_attack += 2
        rupee -= 1
        print(f"Je hebt een zwaard gekocht. en je huidige saldo {rupee}")
    else:
        print("JE hebt niks gekocht.")