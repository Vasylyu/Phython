# Создайте функцию генератор чисел Фибоначчи fibonacci.
# На входе:
# f = fibonacci()
# for i in range(10):
#     print(next(f))
# На выходе:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci(f):
    if f < 0:
        return print("Пожалуйста, введите положительное число")
    elif f == 0:
       return print(f"Если {f} число Фибоначчи: 0")
    first = 0
    second = 1
    if f == 1:
       return print(f"Если один число фибоначи {first}")
    elif f == 2:
        return print(second)

    for i in range(2, f):
        first, second = second, first + second
        print(second)
print(fibonacci(10))

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
f = fibonacci()
for i in range(10):
    print(next(f))