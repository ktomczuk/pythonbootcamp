a = input('Podaj miasto 1: ')
b = input('Podaj miasto 2 ')
c = float(input('Podaj odleglosc '))
d = float(input('Podaj koszt paliwa '))
e = float(input('Podaj spalanie '))

f = c * d * e / 100
print(f'Koszt {a} do {b} {f:.2f}')
g=int(f)
print(f'Koszt 2:{g}')


