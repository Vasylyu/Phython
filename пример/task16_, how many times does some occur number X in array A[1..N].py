
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
N = int(input("Введите расмер массива: "))
array = list()
for i in range (N):
    array.append(random.randint(1, 20))
print(array, end=' ')
x = int(input("число каторое возможно есть в массиве: "))
count = 0
for i in range(len(array)):
    if array[i] == x:
        count = count + 1
print(array)
print("встречается",count, "раз")


