# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UserException(Exception):
    pass

class LevelError(UserException):
    def __init__(self, level, exam):
        self.level = level
        self.exam = exam

    def __str__(self):
        return (f'Уровень пользователя должен быть не ниже{self.exam}.\n'
                f'ваш уровень{self.level}. Ошибка добавления.')

class AccessError(UserException):
    def __init__(self, id_user, name):
        self.id_user = id_user
        self.name = name
    def __str__(self):
        return (f'Введите ID: {self.id_user} и имя пользователя: {self.name} не совпадают'
                f'с имеющимеся вбазе данных. .\nВ доступе отказано')

if __name__ == '__main__':
    try:
        number = int(input('Введите число: '))
        if number < 5:
            raise LevelError(1, 2)
        if 5 <= number < 10:
            raise AccessError(5)
    except ValueError:
        print('не число')
    except LevelError as le:
        print(le)
    except AccessError as ae:
        print(ae)
    else:
        print('ошибки не было')
    finally:
        print("всегда в конце")