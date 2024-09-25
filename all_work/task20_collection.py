
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

from pprint import pprint

corteg = (1,'fggg', 4,6,7,3.05,
          (1,4,5), [5], 'ghjdfdrfr')

dct = {}
for item in corteg:
    key = type(item)
    dct.setdefault(key, []).append(item)
pprint(dct)
