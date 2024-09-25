# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Arсhive:
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

    def __repr__(self):
        """Представление для програмиста"""
        return f"Архив {self.number=}, {self.string=})"

    def __str__(self):
        """Представление для пользователя"""
        return f"Число: {self.number}, Строка: {self.string})"


if __name__ == '__main__':
    a1 = Arсhive(10, 'Привет!')
    a2 = Arсhive(20, 'Как дела?')
    a3 = Arсhive(30, 'Отлично!')
    print(a1)
    print(repr(a1))
    print(a1.get_archive())

