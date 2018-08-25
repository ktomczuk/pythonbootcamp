#i= 1
#sr = 0
liczby = []
#b = list()
#while i <= 10:
#    a = int(input('Podaj liczbe:' ))
#    liczby.append(a)
#    b[i] = a
#    i = i+1
#    sr = sr + a
#x = sum(liczby)
#print(f'srednia to {x/i}')


while len(liczby) < 3:
    a = input('Podaj liczbe:')
    if a == 'k':
        break
    else:
        a = int(a)
        liczby.append(a)
    pass

x = sum(liczby)
srednia = sum(liczby) / len(liczby)
print(f'srednia z liczb {liczby} to {srednia}')