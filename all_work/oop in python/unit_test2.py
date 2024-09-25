# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest



class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = value

class TestRectangle(unittest.TestCase):
    def test1(self):
        self.assertEquals(Rectangle.get_area(Rectangle(7,10)), 70)

    def test2(self):
        self.assertEquals(Rectangle.get_perimeter(Rectangle(5,10)),30)

    

if __name__ == '__main__':
    unittest.main(verbosity=2)
