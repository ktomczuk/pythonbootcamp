x = input('Podaj jakis tekst: ')
slownik = {'1':'1', '2':'2' ,'3':'3' ,'4':'4' ,'5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
licznik = {}
abc = '1234567890 qwertyuiopasdfghjklzxcvbnm'
#for i in x.lower():
#    if i in licznik:
#        licznik[i] += 1
#    else:
#        licznik[i] = 1

#print(licznik)
# slownik zliczanie znakow
for i in x.lower():
    licznik[i] = licznik.get(i, 0) +1

for i in licznik:
    print(f' Liutera {i} wystapila: {licznik[i]}')
