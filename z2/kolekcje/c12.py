sedt = {1,2,3,4,5,6,7,8,9,0}
z = set()
#a = True
#x = int(input('podaj liczbe: '))
#z = z.add(x)
while True:
    x = input('Podaj liczbe: ')
    if x == 'k':
        break
    else:
        x = int(x)
        z.add(x)
#for i in
lp = set(range(0,101,2))
print(f' liczby = {z & lp}')
#y = int(input('podaj liczbe: '))


# lista do kwadratu
f = [12,3,4,5,6]
[f**2 for f in range(5)]
