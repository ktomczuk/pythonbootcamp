Zakres = range(100)  # range(poczatek:koniec:krok)
a = 0
b = 0
c = 0
for i in range(101):
    if i % 3 == 0:
        a += 1
        print(i)
    if i % 5 == 0:
        b += 1
        print(i)
    if i % 3 == 0 or i % 5 == 0:
        c += 1
print(f'Liczb podzielnych przez 3 jest {a}, a przez 5 {b} a podzielnych prze 3 lub 5 {c}')
