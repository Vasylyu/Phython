'''''
Дескрипторы - это атрибуты экземпляра класса 
со связанным поведением, которые обеспечивается 
за счет перегрузки соответсвующих методов (hours, rate)

'''''


class Validate:
    # def __init__(self, atr):
    #     self.atr = atr

    def __get__(self, instance, owner):
        print('полезная нагрузка')
        return instance.__dict__[self.atr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Неверна')
        self.atr = value

    def __set_name__(self, owner, name):
        self.atr = name


class Worker:
    hours = Validate()
    rate = Validate()

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
        


    def calculation(self):
        return self.rate * self.hours

w = Worker(10, 100)
w.hours = 10

  
