# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
class Rentangle:
    def __init__(self, length, width=None):
            self.length = length
            self.width = width if width else length


    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        new_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rentangle(new_perimeter / 4)

    def __sub__(self, other):
        new_perimeter = self.get_perimeter() - other.get_perimeter()
        if new_perimeter < 0:
            return Rentangle(0)
        return Rentangle(new_perimeter / 4)

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

""" отступление """
class NewClass:
    def __call__(self, *args, **kwargs):
        pass
obj = NewClass()
obj()

if __name__ == '__main__':
    rentangle1 = Rentangle(10,5)
    rentangle2 = Rentangle(8, 3)

    rentangle_sum =rentangle1 + rentangle2
    print('Периметр суммы: ', rentangle_sum.get_perimeter())

    rentangle_diff = rentangle1 - rentangle2
    print('Периметр разности ' , rentangle_diff.get_perimeter())
    print(rentangle1 < rentangle2)
    print(rentangle1 <= rentangle2)
    print(rentangle1 == rentangle2)
    print(rentangle1 != rentangle2)
    print(rentangle1 > rentangle2)
    print(rentangle1 >= rentangle2)

    rentangle3 = Rentangle(5,10)
    print(rentangle1 == rentangle3)
