from math import sqrt
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2

square = sqrt(p * (p - a) * (p - b) * (p - c))
print(square)
