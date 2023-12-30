import random

# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


n = int(input('Enter long array: '))
min_number = int(input('min number array: '))
max_number = int(input('max number array: '))
#list2 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list2 = [random.randint(-20, 20) for _ in range(n)]
#list2 = sorted(list1)
# print(list1)
# print()
print(list2)
for i in range(len(list2)):
    if min_number <= list2[i] and max_number >= list2[i]:
        print(i, end= ' ')
        # for i in range(len(list_1)):
        #     if min_number <= list_1[i] <= max_number:
        #         print(i)

