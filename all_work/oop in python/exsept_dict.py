# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_dict(my_dict, my_key, default_value = None):
    try:
        return my_dict[my_key]
    except KeyError:
        return default_value

my_dict = {2: 'qwe', 3: 'rty'}
my_key2 = 2
my_key1 = 1

print(get_dict(my_dict, my_key2))
print(get_dict(my_dict, my_key1))