# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

from json import load, dump
from exsept_file import User
import pytest


class NameError(Exception):
    def __str__(self):
        return f'Ошибка имени'


class LevelError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Ошибка уровня'



class Repo:
    users = []

    @staticmethod
    def load_users():
        with open('user.json', 'r', encoding='utf-8') as f:
            data = load(f)
        for level, value in data.items():
            for id, name in value.items():
                Repo.users.append(User(name, id, level))

    @staticmethod
    def check_login(name):
        try:
            for user in Repo.users:
                if user.name == name:
                    return f'{name} Пользователь найден'
            raise NameError
        except NameError:
            return "Пользователь не найден"

    @staticmethod
    def create_user(name, id_user, level):
        try:
            if level > 3:
                raise LevelError
        except LevelError:
            return 'Ошибка уровня'
        else:
            Repo.users.append(User(name, id_user, level))

    @staticmethod
    def get_login_level(name):
        for el in Repo.users:
            if name == el.name:
                return 'Пользователь найден'
            raise NameError()


@pytest.fixture
def func():
    obj = Repo()
    obj.load_users()
    return obj

def test_access(func):
    assert func.get_login_level('Новиков') == 'Пользователь найден'

def test_except(func):
    with pytest.raises(NameError):
        func.get_login_level('НОвиков')

if __name__ == '__main__':
    pytest.main(['-v'])