tekst = str(input('Podaj tekst: '))
licznik = {}
for i in tekst:
    licznik[i] = licznik.get(i, 0) + 1

for i in licznik:
    if licznik[i] >= 2:
        print(f' Litera {i} wystapila: {licznik[i]}')