i = 0
l = 0
while True:
	liczba = input(f'Podaj liczbę {i}: ')
	if liczba == 'koniec':
		print('koniec wczytywania')
		break
	else:
		l += int(liczba)
		i += 1
print(f'Srednia wynosi : {l / i}, suma wynosi {l}, ilosc liczb {i}')

	
