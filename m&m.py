import  random

kleuren = ['oranje', 'blauw', 'groen', 'bruin']
hoeveelheid = input('Hoeveel M&Ms wil je in de zak? ')

def zakVullen(aantal):
    zak = []
    for x in range(int(aantal)):    
        keuze = random.choice(kleuren)
        zak.append(keuze)
    return zak
print('\nInhoud zak: \n')
print(sorted(zakVullen(hoeveelheid)))