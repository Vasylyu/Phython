# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print
result = None

while True:
    number = int(input("enter number from 1 to 999: "))
    if number == 0:
        break
    elif  number < 1 or number > 999:
        print("число в не диапозона")
        continue
    elif number < 10:
        result = number ** 2
    elif number < 100:
        result = (number % 10) * (number // 10)
    elif number < 1000:
        last = number % 10
        number //= 10
        middle = number % 10
        first = number // 10
        result = last * 100 + middle * 10 + first
    print(f'result: {result}')
