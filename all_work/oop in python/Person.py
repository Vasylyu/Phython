# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:

    def __init__(self, name, age, phone):
        self.__name = name
        self.__age = age
        self.__phone = phone

    def birthday(self):
        self.__age += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

p = Person('Иван',33, '8-907-24-234')
print(f'{p.name} / {p.age} / {p.phone}')
p.birthday()
print(f'{p.name} / {p.age} / {p.phone}')
