
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def number_n(number: int):
#     if number in (1, 2, 3, 4, 5, 6):
#         return number - 1
#     return (number_n(number + 1) == number:
#     return (number_n(number) == number:
#
# print(number_n(1, 2, 3, 4, 5, 6))
n = 6
def rec_input(num: int):
   if num == 0:
       return ' '
   s = input("Введит что-нибудь: ")
   return rec_input(num-1) + s + " "
print(rec_input(n))

# def funk(num):
#     number = input()
#     if num == 1:
#         return number
#     return funk(num - 1) + ' ' + number
#
#
# n = int(input('Введите число: '))
# print(funk(n))