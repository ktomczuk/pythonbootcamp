i = 0
l = 0
while True:
	liczba = str(input(f'Podaj liczbę {i}: '))
	if liczba == 'koniec':
		break
	else:
		l[i] = int(liczba)
		i += 1
j = 1
while j>=i:
	j += 1
	min = l[i] 
	max = l[i]
	if l[i] < min:
		min = l[i]
	if l[i] > max:
		max = l[i]

print(f'Liczba max to {max} liczba min to {min}') 
	
  


	
