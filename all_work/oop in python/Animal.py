# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Fish:

    def __init__(self, genius, age, dept_of_swimming):
        self.__genius = genius
        self.__age = age
        self.__dept_of_swimming = dept_of_swimming

    def info(self):
        return (f'Вид: {self.__genius}, возраст: {self.__age}, '
                f'глубина плвания: {self.__dept_of_swimming} м')

class Bird:
    def __init__(self, genius, age, height_of_flying):
        self.__genius = genius
        self.__age = age
        self.__height_of_flying = height_of_flying

    def info(self):
        return (f'Вид: {self.__genius}, возраст: {self.__age}, '
                f'высота полета: {self.__height_of_flying} м')

class Mammal:
    def __init__(self, genius, age, speed):
        self.__genius = genius
        self.__age = age
        self.__speed = speed

    def info(self):
        return (f'Вид: {self.__genius}, возраст: {self.__age}, '
                f'скорость бега: {self.__speed} км/ч')

f = Fish('Окунь', 1, 2)
b = Bird("Орел",2,150)
m = Mammal("Лев",7,60)
print(f.info())
print(b.info())
print(m.info())