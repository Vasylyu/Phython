
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

import random

n = int(input('Список первый задай: '))
list1 = [random.randint(1,15) for _ in range(n)]
print(list1)
count = 0
for i in range(1,len(list1)-1):
    if list1[i-1] < list1[i] > list1[i + 1]:
        count += 1
print(count)

# import random
#
# len1 = int(input("Размер список: "))
# lst1 = [random.randint(0, 10) for _ in range(len1)]
# print(lst1)
# count = 0
# for i in range(1, len1 - 1):
#     if lst1[i] > lst1[i - 1] and lst1[i] > lst1[i + 1]:
#         count += 1
#
#
# # list comprehension
# result = [1 for i in range(1, len1 - 1) if lst1[i] > lst1[i - 1] and lst1[i] > lst1[i + 1]]
#
# print(count)
# print(result.count(1))