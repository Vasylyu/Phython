
# Требуется найти в массиве list_1 самый близкий по значению элемент
# к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

lenlst = int(input("Введите длину списка: "))
delta = 10000
lst = []

for i in range(lenlst):
    lst.append(random.randint(1, 100))

print(lst)

x = int(input("Введите число X: "))
for i in range(len(lst)):
    delta_x = x - lst[i]
    if delta_x < 0:
        delta_x *= -1
    if delta_x < delta:
        delta_i = i
        delta = delta_x

print(f'Самый близкий по величине элемент, число: {lst[delta_i]}')

