x = str(input('Wpisz jakis napis: '))
y = 0
z = 0
SAMOGLOSKI = "aeiouy"
for i in range(len(x)):
    if x[i] == 'a' or x[i] == 'o' or x[i] == 'e' or x[i] == 'i' or x[i] == 'u' or x[i] == 'y':
        y += 1

for i in x.lower():
    if i in SAMOGLOSKI:
        z += 1

print(f'Ilosc aeouiy wynosio : {y}{z}')

print(x.count('a') + x.count('o') + x.count('u') + x.count('y') + x.count('i') + x.count('e'))

# lancuchowe laczenie
x.strip(x)
