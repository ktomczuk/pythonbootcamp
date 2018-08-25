imiona = ['kamil', 'piotrek', 'romek', 'gucio', 'wiola'] # listy sa w kwadratach

print(imiona)
print(len(imiona))
print(type(imiona))
print('kamil' in imiona)
for imie in imiona:
    print(imie)

print('imie z indexu: ', imiona[0])
print('Ostatnie imie to ', imiona[-1])
print('Przedstatnie imie to ', imiona[-2])
print('imiona 0-2 ', imiona[0:2])

print(dir(imiona))

imiona.append('koza') #rozszerza liste
print(imiona)
imiona.pop('kamil') # dropuje, pusta dropuje ostatnia
print(imiona)
