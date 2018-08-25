x = str(input('Wpisz jakis napis: '))
k = p = 0
for i in x:
    if i == "<":
        p = i
    if i == ">":
        k = i
#z = k - p
#print(f'liczba znakow powmiedzy to: {z}')
for i in range(len(x)):
    if x[i] == "<":
        p = i
    if x[i] == ">":
        k = i
z = k - p - 1
print(f'liczba znakow powmiedzy to: {z}')

p1 = x.rfind("<")
k1 = x.rfind(">")
z1 = k1 - p1 - 1
print(f'liczba znakow powmiedzy to: {z1}')