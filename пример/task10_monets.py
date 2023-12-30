
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
n = int(input("Введите количество монет: "))
eagle = 1
tails = 1
coins = 0

for _ in range(n):
    monets = random.randint(0,1)
    print(monets, end=" ")
    for _ in range(eagle):
        coins += 1
    for _ in range(tails):
        coins += 1
    if eagle > tails:
        coins = tails
    elif tails > eagle:
        coins = eagle

print()
print(coins)