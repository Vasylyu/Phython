
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
import random
lst_orbit_a = [random.randint(1, 20) for _ in range(10)]
print(lst_orbit_a)
lst_orbit_b = [random.randint(1, 20) for _ in range(10)]
print(lst_orbit_b)
lst_orbit_c = list(zip(lst_orbit_a, lst_orbit_b))
print(lst_orbit_c)
def orbit_x(lst_orbit_c):
    qvadrat = [(i[0] != i[1])*i[0]*i[1] for i in lst_orbit_c]
    return lst_orbit_c[qvadrat.index(max(qvadrat))]
print(*orbit_x(lst_orbit_c))


# from random import randint
# print(planets := [(randint(1,10),randint(1,10)) for _ in range(10)])
# print(planets := set(filter(lambda x:[0] != x[1], planets)))
# print(sorted(planets, key=lambda x: x[0] * x[1], reverse=True))