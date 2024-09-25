# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging


logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno}'
                    'функция "{funcName}()" : {msg}', style='{', level=logging.WARNING)

def func(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logging.warning('не дели на ноль тупица')
        return ''
    else:
        return res

print(func(5,0))
