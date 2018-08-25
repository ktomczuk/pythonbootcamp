list = [1, 2, 3, -4, -2, 9, 8, 7, 8]
a = 0
b = 0

for i in range(len(list)):
    if list[i] > 0:
        a += 1
    else:
        b += 1
print(f'Liczb dodanich jest {a}, a ujemnych {b}')
