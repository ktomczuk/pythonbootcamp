Z = (1, 2, 3, 4, 5, 6, 7, 7, 7, 7)
print('Drugi element', Z[1])
print('Przedostatni: ', Z[-2])
print('Zbior od 3 do 7', Z[2:7])
print('co trzeci', Z[::3])
print('co druga od tylu', Z[::-2])
print('co druga od tylu', Z[::-2])
print('od 2ej do 7ej ze skokiem 3 ', Z[1:7:3])
#pusta tupla
x = tuple()
print(type(x))
dir(x) # ,etody ktorych mozn uzyc w konsoli i potemmoyna y nic jechac jak w pryzkdyi eponiyej

print('zliczanie', Z.count(7))