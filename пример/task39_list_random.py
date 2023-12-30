
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

import random
n = int(input('Список первый задай: '))
n2 = int(input('Список второй задай: '))
list1 = [random.randint(1,15) for _ in range(n)]
list2 = [random.randint(1,15) for _ in range(n2)]
print(list1)
print(list2)

change = set(list1).difference(list2)
print(change)
for i in list1:
    if i in change:
        print(i, end= ' ')
# result = [i for i in list1 if i in change]
# print(result)