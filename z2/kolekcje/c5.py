list = [5, 2, 1, 4, 3]

max = list[0]
min = list[0]
imax = 0
imin = 0

for i in range(len(list)):
    if list[i] > max:
        max = list[i]
        imax = i
    if list[i] < min:
        min = list[i]
        imin = i

print(list)
list[imin] = max
list[imax] = min
print(list)
list[imin], list[imax] = list[imax], list[imin]
print(list)

