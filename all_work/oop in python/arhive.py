# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

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


if __name__ == '__main__':
    a1 = Arсhive(10, 'Привет!')
    a2 = Arсhive(20, 'Как дела?')
    a3 = Arсhive(30, 'Отлично!')
    print(a1.get_archive())
    print(a2.numbers_archive)
    print(a3.string_archive)
