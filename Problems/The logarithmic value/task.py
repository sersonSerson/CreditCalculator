from math import log

first = int(input())
second = int(input())

if second == 0 or second == -1 or second < 0:
    print(round(log(first), 2))
else:
    print(round(log(first, second), 2))
