# Доработайте задачу Animal
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, genius, age):
        self.__genius = genius
        self.__age = age

    def get_genus(self):
        return self.__genius

    def get_age(self):
        return self.__age

    def info(self):
        return f'Вид: {self.__genius}, возраст: {self.__age} лет'

class Fish(Animal):

    def __init__(self, genius, age, dept_of_swimming):
        super().__init__(genius, age)
        self.__dept_of_swimming = dept_of_swimming

    def info(self):
        return (f'{super().info()} глубина плвания: {self.__dept_of_swimming} м')

class Bird(Animal):
    def __init__(self, genius, age, height_of_flying):
        super().__init__(genius, age)
        self.__height_of_flying = height_of_flying

    def info(self):
        return (f'{super().info()} '
                f'высота полета: {self.__height_of_flying} м')

class Mammal(Animal):
    def __init__(self, genius, age, speed):
        super().__init__(genius, age)
        self.__speed = speed

    def info(self):
        return (f'{super().info()}'
                f' скорость бега: {self.__speed} км/ч')

f = Fish('Окунь', 1, 2)
b = Bird("Орел",2,150)
m = Mammal("Лев",7,60)
print(f.info())
print(b.info())
print(m.info())