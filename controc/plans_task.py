# Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta
def future_date(days_from_now):
    today = datetime.now()
    future_date = today + timedelta(days=days_from_now)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date

if __name__ == '__main__':
    days = 100
    print(f'Дата через {days} дня(дней) от сегодня это {future_date(days)}')