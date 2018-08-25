from random import randint
zakres = 10
i = 0
x = randint(1, zakres)
print(f' Wylosowan liczba1 {x}')
y = randint(1, zakres)
print(f' Wylosowan liczba2 {y}')
while True:
	xy = int(input('Podaj iloczyn dwóch liczb: '))
	i +=1
	if xy == x*y:
		print(f'Kuniec iloczyn to {x*y} podales to w probie {i}')
		break
		
		