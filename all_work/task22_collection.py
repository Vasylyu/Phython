#  Создайте вручную список с повторяющимися целыми числами.
#  Сформируйте список с порядковыми номерами
#  нечётных элементов исходного списка.
#  Нумерация начинается с единицы.

my_list = [1, 2, 3, 3, 4, 5, 5, 5, 6, 9, 9, 11, 11, 12]
new_list = []
for index, value in enumerate(my_list):
    if (value % 2) != 0:
        new_list.append(index + 1)
print(new_list)

print([index + 1 for index, value in enumerate(my_list) if (value % 2) != 0])
