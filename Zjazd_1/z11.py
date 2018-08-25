a = int(input('Podaj liczbe x 0 do 100: '))
b = int(input('Podaj liczbe y 0 do 100: '))
#c = input(' Podaj operacje (+, -, *, /) :')
if  a <=0 and a>=101:
	wynika='Poza planszą'
elif 0<=a<=9:
	wynika='Lewy'
elif 10<=a<=90:
	wynika='Centrum'
elif 91<=a<=100:
	wynika='Prawy'
else:
	wynika='Ośle traf w cyferke'
if  b <=0 and b>=101:
	wynikb='Poza planszą'
elif 0<=b<=9:
	wynikb='Gora'
elif 10<=b<=90:
	wynikb='Centrum'
elif 91<=b<=100:
	wynikb='Dol'
else:
	print('Ośle traf w cyferke')
print(f'Jestes {wynika} {wynikb}')
