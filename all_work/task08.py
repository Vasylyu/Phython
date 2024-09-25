
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#  *
#  ***
#  *****
#  *******
# *********

space = ' '
elem = '*'
rows = int(input('Введите количество столбов в елке: '))
spaces = rows - 1
elems = 1
for _ in range(rows):
    print(space * spaces + elem * elems + space)
    elems += 2
    spaces -= 1