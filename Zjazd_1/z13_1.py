dzien = 0
temp = 0
sr = 0
while dzien <= 6:
	temp = float(input('Podaj dzisiejsza temp '))
	dzien += 1
	sr += temp
	print(f'Temp {sr / dzien} dzien {dzien}')

print(f'temp srednia: {sr / 7}')