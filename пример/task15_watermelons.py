#Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random
usernum = int(input("Введите количество арбузов: "))
maximilians = 0
minimilian = 30
for _ in range(usernum):
    mass_watermelon = random.randint(1,30)
    print(mass_watermelon, end=" ")

    if maximilians < mass_watermelon:
        maximilians = mass_watermelon
    elif minimilian > mass_watermelon:
        minimilian = mass_watermelon
print()
print(minimilian, maximilians)