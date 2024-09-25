"""
Задание 1. Отцы, матери и дети.
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
● имя,
● возраст,
● список детей.
И он может:
● сообщить информацию о себе,
● успокоить ребёнка,
● покормить ребёнка.
У ребёнка есть:
● имя,
● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
● состояние спокойствия,
● состояние голода.
Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
и словарь состояний, и что-то поинтереснее
"""


class Parents:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_children = []


    def add_child(self, child):
        if self.age - child.age >= 16:
            self.list_children.append(child)
            print(f"Ребёнок {child.name} добавлен к {self.name}.")
        else:
            print(f"Ребёнок {child.name} не добавлен к {self.name} "
                  f"так как разница в возрасте слишком мала.")

    def feed(self, child):
        if child in self.list_children:
            child.hungry = False
            print(f"{self.name} покормил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def calm(self, child):

        if child in self.list_children:
            child.calm = True
            print(f"{self.name} успокоил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def list_childrens(self):

        if self.list_children:
            print(f"У {self.name} есть следующие дети:")
            for child in self.list_children:
                print(f" - {child}")
        else:
            print(f"У {self.name} нет детей.")


    def __repr__(self):
        return (f"Родитель: ('{self.name}', '{self.age}')")


class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.self_calm = False
        self.self_hangrid = True

    def get_status(self):

        calm_status = "спокоен" if self.calm else "не спокоен"
        hungry_status = "сыт" if not self.hungry else "голоден"
        print(f"Ребёнок {self.name} {calm_status} и {hungry_status}.")

    def __repr__(self):
        return (f"Ребенок: ('{self.name}', '{self.age}'),")


    # def calm(self):
    #     if self_calm < 5:
    #         return f'Ребенка надо успокоить'
    #     else:
    #         return f'Ребенок счастлив'
    #
    # def feed(self):
    #     if self_hangrid < 5:
    #         return f'Ребенка надо покормить'
    #     else:
    #         return f'Ребенок сыт'


p1 = Parents('Анна',35)
p2 = Parents('Василий',32)
c1 = Child("Фиона", 10)
c2 = Child("Федя", 12)
c3 = Child("Катя", 9)

for child in [c1, c2]:
    p1.add_child(child)

for child in [c3]:
    p2.add_child(child)
print(p1, p2.__repr__())
print(c1,c2,c3.__repr__())

p1.list_childrens()
p2.list_childrens()

for child in p1.list_children:
    p1.feed(child)
    p1.calm(child)
    child.get_status()

for child in p2.list_children:
    p2.feed(child)
    p2.calm(child)
    child.get_status()

