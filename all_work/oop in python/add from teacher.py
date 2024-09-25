class Worker:

    def __init__(self, hours, rate):
        if hours < 0:
            raise ValueError('Недопустимо число часов')
        if hours < 0:
            raise ValueError('Недопустима ставка')
        self.__hours = hours
        self.__rate = rate

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if value < 0:
            raise ValueError('Недопустимо число часов')
        self.__hours = value

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        if value < 0:
            raise ValueError('Недопустима ставка')
        self.__rate = value


    def calculation(self):
        return self.__rate * self.__hours

w = Worker(10,100)
print(w.calculation())
w.hours = -10
print(w.calculation())