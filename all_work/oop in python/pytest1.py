# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
from func_primer import convert_str
import pytest
def test1():
    assert convert_str('hello world') == 'hello world', 'ошибка 1'

def test2():
    assert convert_str('HELLO world') == 'hello world', 'ошибка 2'

if __name__ == '__main__':
    pytest.main(['-v'])



