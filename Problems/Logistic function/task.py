from math import exp

x = int(input())

logistic = 1 / (1 + exp(-x))
print(round(logistic, 2))
