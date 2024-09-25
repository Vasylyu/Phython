# Напишите функцию key_params, принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример использования.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

# res = {}
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# params2 = params.split(',')
# for elem in params2:
#     mid_idx = len(str(elem)) // 2
#     key = (str(elem)[mid_idx:])
#     value = (str(elem)[:mid_idx])
#     res[key] = value
# print(res)


def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result


print(key_params(a=1, b='hello', c=[1, 2, 3], d={}, g= 0.5))
