# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

def redactor(text):
    result = text.lower()
    for el in result:
        if ord(el) != 32:
            if ord(el) < 97 or ord(el) > 122:
                result = result.replace(el, '')
    return result

text ="ferferfgerjg 453534543,feferf..ewfref345345JJJHGGFHG"
print(redactor(text))
