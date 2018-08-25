cennik = {
    'j': '12',
    'g': '20',
    'c': '5',
    'p': '1'
}

stan = {
    'j': '100',
    'g': '2',
    'c': '10',
    'p': '1'
}
Koszyk = 0
print('Witamy w cebula sklep')
z = str(input('Chcesz cos kupic (Tak/Nie): '))
while z == 'Tak':

    for i in cennik:
        print(f'Produkt {i} w cenie {cennik[i]} PLN')
    x = input('Podaj co:')
    y = int(input('Podaj ile:'))
    Koszyk = Koszyk + float(cennik[x])*y
    Paragon = y.getattribute
    Paragon = x.getitem
    #stan =
    print(f'Masz do zabulenia {float(cennik[x])*y} PLN')
    z = str(input('Chcesz cos kupic (Tak/Nie): '))
