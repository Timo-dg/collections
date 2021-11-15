import random

kleuren = ['oranje', 'blauw', 'groen', 'bruin']
hoeveelheid = input('Hoeveel M&Ms wil je in de zak? ')

def zakVullen(aantal:int):
    zak = {}
    for x in range(int(aantal)):    
        kleur = random.choice(kleuren)
        if kleur in zak:
            zak[kleur] += 1
        else:
            zak.update({kleur : 1})
    return zak

print('\nInhoud zak: \n')
print(sorted(zakVullen(hoeveelheid).items(), key= lambda kv:kv[1], reverse= True))