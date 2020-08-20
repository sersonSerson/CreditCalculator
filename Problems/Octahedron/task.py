from math import sqrt
side = float(input())
area = round(2 * sqrt(3) * side ** 2, 2)
volume = round(1 / 3 * sqrt(2) * side ** 3, 2)
print(f'{area} {volume}')
