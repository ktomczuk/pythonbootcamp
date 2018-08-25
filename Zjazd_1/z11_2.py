x = int(input('Podaj liczbe x 0 do 100: '))
y = int(input('Podaj liczbe y 0 do 100: '))
if x<=0 or x>=100 or y<=0 or y>=100:
	print('jestes poza plansza')
elif x>=0 and x<=9:
	if y>=0 and y<=9:
		print('LG')
	elif y>=10 and y<=90:
		print('L')
	elif y>90 and y<100:
		print('LD')+
elif x>=10 and x<=90:
	if y>=0 and y<=9:
		print('G')
	elif y>=10 and y<=90:
		print('C')
	elif y>90 and y<100:
		print('D')
elif x>=90 and x<=100:
	if y>=0 and y<=10:
		print('PG')
	elif y>=10 and y<=90:
		print('P')
	elif y>90 and y<100:
		print('PD')