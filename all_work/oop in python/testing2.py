# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов


def redactor(text):
    '''

    >>> redactor('hello world')
    'hello world'

    '''
    result = text.lower()
    for el in result:
        if ord(el) != 32:
            if ord(el) < 97 or ord(el) > 122:
                result = result.replace(el, '')
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()