# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import date
import logging

logging.basicConfig(filename='example_3.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.ERROR)


def user_date(data_text):
    dict_month = {'январь': 1, 'февраль': 2, 'март': 3,
                  'апрель': 4, 'май': 5, 'июнь': 6,
                  'июль': 7, 'август': 8, 'сентябрь': 9,
                  'октябрь': 10, 'ноябрь': 11, 'декабрь': 12.}

    dict_days = {'понедельник': 1, 'вторник': 2, 'среда': 3, 'четверг': 4,
                 'пятница': 5, 'суббота': 6, 'воскресенье': 7}
    try:
        data_text = data_text.split()
        num_week, day, month = int(data_text[0][0]), int(dict_days[data_text[1]]), \
            int(dict_month[data_text[2]])
    except ValueError:
        logging.error('некоректный формат данных')
        return "некоректный формат данных"

    data_month = month
    data_year = date.today().year

    first_day_data_month = date(data_year, data_month, 1).weekday()

    if first_day_data_month >= day:
        data_day = (7 - first_day_data_month) + (num_week - 1) * 7 + day
    else:
        data_day = (7 - first_day_data_month) + (num_week - 2) * 7 + day
    try:
        data = date(data_year, data_month, data_day)
    except ValueError:
        logging.error('нет такого дня в этом месяце')
        return "нет такого дня в этом месяце"

    return data


dates = ['1-й четверг ноябрь',
         '3-й суббота январь',
         'опять вторник в март',
         '2-я среда май',
         '2-й четверг апрель']
for el in dates:
    print(user_date(el))
