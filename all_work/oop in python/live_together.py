"""
Задача 2. Совместное проживание
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
одиночестве, Артём решил провести необычное исследование. Для этого он
реализовал модель человека и модель дома.
Человек может (должны быть такие методы):
● есть (+ сытость, − еда);
● работать (− сытость, + деньги);
● играть (− сытость);
● ходить в магазин за едой (+ еда, − деньги);
● прожить один день (выбирает одно действие согласно описанному ниже
приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):
● имя,
● степень сытости (изначально 50),
● дом.
В доме есть:
● холодильник с едой (изначально 50 еды),
● тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.
Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6.
2. Если сытость < 20, то нужно поесть.
3. Иначе, если еды в доме < 10, то сходить в магазин.
4. Иначе, если денег в доме < 50, то работать.
5. Иначе, если кубик равен 1, то работать.
6. Иначе, если кубик равен 2, то поесть.
7. Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.
Реализуйте такую программу и создайте двух людей, живущих в одном доме.
Проверьте работу программы несколько раз.
"""
import random


class House:
    def __init__(self, freez_food = 50, case_money = 0):
        self.freez_food = freez_food
        self.case_money = case_money

    def buy_food(self, quantity, price):
        if self.case_money >= price:
            self.freez_food += quantity
            self.case_money -= price
            print(f'Купили {quantity} единиц еды за {price} денег')
        else:
            print('Недостаточно денег на еду!')

    def earn_money(self, salary):
        self.case_money += salary
        print(f'Заработали {salary} денег.')


class Human:
    def __init__(self, name, home):
        self.name = name
        self.hungry_status = 50
        self.home = home

    def eat(self):
        if self.home.freez_food >= 10:
            self.hungry_status += 10
            self.home.freez_food -= 10
            print(f'{self.name} полел. Сытость увеличилась до {self.hungry_status}, '
                  f'еда уменьшилась до {self.home.freez_food}')
        else:
            print(f'{self.name} хотел поесть, но в доме мало еды')

    def work(self):
        self.hungry_status -= 10
        self.home.earn_money(50)
        print(f'{self.name} поработал. Сытость уменьшилась до {self.hungry_status}.')

    def play_game(self):
        self.hungry_status -= 5
        print(f'{self.name} поиграл. Сытость уменьшилась до {self.hungry_status}.')

    def go_to_food(self):
        self.home.buy_food(15, 50)

    def live_one_day(self):
        cub = random.randint(1, 6)
        print(f'\nСегодняшний кубик: {cub}')

        if self.hungry_status < 20:
            self.eat()

        elif self.home.freez_food < 10:
            self.go_to_food()

        elif self.home.case_money < 50:
            self.work()

        elif cub == 1:
            self.work()
        elif cub == 2:
            self.eat()
        else:
            self.play_game()

        if self.hungry_status <= 0:
            print(f'{self.name} умер от голода.')
            return False
        return True


house1 = House()

human1 = Human('Filip', house1)
human2 = Human('Дашка', house1)

house2 = House()

human3 = Human('Толян', house2)
human4 = Human('Машка', house2)

try:
    for day in range(1, 366):
        print(f'\nДень {day}')
        if not human1.live_one_day() or not human2.live_one_day() or not human3.live_one_day() or not human4.live_one_day():
            print(f'Человек умер на {day} день')
            break

finally:
    print('\nСостояние пары:')
    print(f"Еда в холодильнике - {house1.freez_food}, Деньги -{house1.case_money}")
    print(f"Состояние {human1.name}: Сытость - {human1.hungry_status}")
    print(f"Состояние {human2.name}: Сытость - {human2.hungry_status}\n")
    print("Состояние одиночки:")
    print(f"Еда в холодильнике - {house2.freez_food}, Деньги -{house2.case_money}")
    print(f"Состояние {human3.name}: Сытость - {human3.hungry_status}")
