# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.
from datetime import datetime
def display_current_datetime():

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    print(f'сечас: {formatted_date}')
    print(f'день недели: {day_of_week}')
    print(f'номер недели в году: {week_number}')
if __name__ == '__main__':
    display_current_datetime()
