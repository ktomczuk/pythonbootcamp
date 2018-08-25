from random import randint
zakres = 9
x = randint(0, zakres)
y = randint(0, zakres)
x1 = randint(0, zakres)
y1 = randint(0, zakres)
i = 0
z = 0
print(f' Twoje połozenie to x , y {x1, y1}')
while True:
	if x1 == x and y1 == y:
		print(f' wygrales, polozenie skarbu to {x, y} w {i} ruchach')
		break
	else:
		z = abs(x1-x) + abs(y1-y)
		print(f' Pozostalo Ci {z} kroków')
		i += 1
	yr = xr = 0
	r = input(f'Twoja pozycja to {x1}, {y1} aby sie poruszyć sie  a, s, d, w: ')
	if str(r) == 'a':
		yr = -1
		if 0<=y1+yr<=9:
			y1=y1+yr
		else:
			y1=y1
		print('wyszedles poza zakres')
	elif str(r) == 'd':
		yr = 1
		if 0<=y1+yr<=9:
			y1=y1+yr
		else:
			y1=y1
		print('wyszedles poza zakres')
	elif str(r) == 'w':
		xr = 1
		if 0<=x1+xr<=9:
			x1=x1+xr
		else:
			x1=x1
		print('wyszedles poza zakres')
	elif str(r) == 's':
		xr = -1
		if 0<=x1+xr<=9:
			x1=x1+xr
		else:
			x1=x1
		print('wyszedles poza zakres')
	else:
		print('Podaj poprawny ruch')

	
	
		
	
	
	
	
