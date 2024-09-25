# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов

from func_primer import convert_str

import unittest

class TestCaseName(unittest.TestCase):
    def test1(self):
        self.assertEquals(convert_str('hello world'), 'hello world')

    def test2(self):
        self.assertEquals(convert_str('HELLO world'), 'hello world')

if __name__ == '__main__':
    unittest.main(verbosity=2)

