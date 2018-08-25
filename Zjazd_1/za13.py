skarbonka = int(input('Podaj ile hajsu bylo od dziadka: '))
while  skarbonka <= 100:
	a = int(input('Podaj ile hajsu dajesz: '))
	skarbonka += a
	print(f'Chajs wrzucony {a}')
	print(f'Chajs w skarbonce {skarbonka}')