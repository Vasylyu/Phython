# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0
count = 0
while True:
    if balance > 5000000:
        print('С вас сняли налог на богатсво!')
        balance -= balance * 0.1
    action = int(input('Введите тип действия: 1- пополнение, 2 - снятие, 0 - выход '))
    if action == 0:
        print(balance)
        break
    elif action == 1:
        sum_add = int(input('Введите сумму пополнения: '))
        if sum_add % 50 == 0:
            balance += sum_add
            count += 1
            if count % 3 == 0:
                balance *= 1.03
        else:
            print('Число не кратное 50-ти у.е!')

    elif action == 2:
        sum_out = int(input('Введите сумму cнятия: '))
        comission = sum_out * 0.015
        if comission < 30:
            comission = 30
        elif comission > 600:
            comission = 600

        if comission + sum_out > balance:
            print('Недостаточно средств!')
        else:
            if sum_out % 50 == 0:
                balance += sum_out + comission
                count += 1
                if count % 3 == 0:
                    balance *= 1.03
            else:
                print('Число не кратное 50-ти у.е!')
    print(balance)
