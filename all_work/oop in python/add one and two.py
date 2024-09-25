# Добавьте к задачам 1 и 2 строки документации для классов.
import time


class MyString(str):
    """ Класс наследующий от str с доп атрибутами
     автора и времени создания
    """

    def __new__(cls, string, author, creation_time=None):
        """
        создает новый обект класса MyString
        """
        if creation_time is None:
            creation_time = time.time()
        obj = super().__new__(cls, string)
        obj.author = author
        obj.creation_time = creation_time
        return obj

    def __str__(self):
        """Возвращает строковое представление"""
        return '{0} {1} {2}'

    def __repr__(self):
        return f"MyString('{self}', author='{self.author}', creation_time ={self.creation_time}"



class Arсhive:
    """Класс для хранения пары свойств и сохранения истории"""
    numbers_archive = []
    string_archive = []
    last_num = None
    last_str = None

    def __init__(self, number, string):
        """ инициализирует новый экземпляр архива"""
        self.number = number
        self.string = string

        if Arсhive.last_num is not None:
            Arсhive.numbers_archive.append(Arсhive.last_num)
        if Arсhive.last_str is not None:
            Arсhive.string_archive.append(Arсhive.last_str)

        Arсhive.last_num = number
        Arсhive.last_str = string

    def get_archive(self):
        return list(zip(Arсhive.numbers_archive, Arсhive.string_archive))


if __name__ == '__main__':
    my_str = MyString("Это моя строка!", "Иван Иванов")
    print(my_str.__repr__())
    print(len(my_str))
    print(my_str.upper())
    print(my_str.title())
    print(my_str)
    a1 = Arсhive(10, 'Привет!')
    a2 = Arсhive(20, 'Как дела?')
    a3 = Arсhive(30, 'Отлично!')
    print(a1.get_archive())
    print(a2.numbers_archive)
    print(a3.string_archive)
    print(Arсhive.__doc__)
    

