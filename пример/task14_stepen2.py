
#Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N
# 10 -> 1 2 4 8

from math import log2, floor
n = int(input("Введите число: "))

print(*[2 ** k for k in range(floor(log2(n)) + 1)])


