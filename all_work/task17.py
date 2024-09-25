# На вход автоматически подаются две строки frac1 и frac2
# вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.
#
# Пример
# На входе:
#
# frac1 = "1/2"
# frac2 = "1/3"
# На выходе:
#
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

import fractions
frac1 = "1/2"
frac2 = "1/3"
# fr1 = frac1.split('/')
# fr2 = frac2.split('/')
# fr1 = [int(item) for item in fr1]
# print(fr1)
# fr2 = [int(item) for item in fr2]
# print(fr2)
# fr1 = fractions.Fraction(1, 2)
# fr2 = fractions.Fraction(1, 3)
# print('Сумма дробей:', fr1 + fr2)
# print('Произведение дробей:', fr1 * fr2)

numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)
print(numerator1,denominator1)
print(numerator2,denominator2)
common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

