
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# Ввод:   Вывод:
# 300     220 284

# def sum_div(n:input('enter number: ')):
#     i = 1
#     a = []
#     while i ** 2 <= n:
#         if n % i == 0:
#             a.append(i)
#             if i != n // i:
#                 a.append(n // i)
#     i += 1
#     a.sort()
#     return sum_div(i)
# def find_frieds(sum_item: int):
#     for i in range(1, (sum_item) +1):
#         var = sum_div(i)
#         if var <= sum_item:
#             if sum_div(var) ==i:
#                 if i < var:
#                     print(i, var)
# find_frieds(10000)

def sum_dividers(number: int):
    dividers = set()
    dividers.add(1)
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            dividers.add(i)
            dividers.add(number // i)

    return sum(dividers)

def find_friendly(max_number: int):
    for i in range(1, max_number + 1):
        var = sum_dividers(i)
        if var <= max_number:
            if sum_dividers(var) == i:
                if i < var:
                    print(i, var)
find_friendly(100000)


#
# def sum_of_divisors(num: int) -> int:
#     summ = {1}
#     for div in range(2, int(num ** 0.5) + 1):
#         if not num % div:
#             summ.add(div)
#             summ.add(num // div)
#     return sum(summ)
#
# friendly_dict = {i: sum_of_divisors(i) for i in range(1, 1000000)}
#
# for number, summ in friendly_dict.items():
#     if number == friendly_dict.get(summ) and number < summ:
#         print(number, summ)
#







