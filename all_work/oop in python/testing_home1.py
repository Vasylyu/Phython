"""
Тестирование класса с использованием pytest
Напишите класс BankAccount, который управляет балансом счета. Он должен
поддерживать следующие методы:
● deposit(amount): добавляет указанную сумму к балансу.
● withdraw(amount): снимает указанную сумму с баланса, если достаточно
средств.
● get_balance(): возвращает текущий баланс счета.
При попытке снять больше средств, чем доступно на счете, должно
выбрасываться исключение InsufficientFundsError. Напишите как минимум
5 тестов для проверки работы классов и его методов.
"""
import pytest


class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__('Недостаточно средств на счету.')


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительна!")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError
        self.balance -= amount

    def get_balance(self):
        return self.balance


@pytest.fixture
def bank_account():
    return BankAccount(100)


def test_initial_balance(bank_account):
    # Проверка начального баланса
    assert bank_account.get_balance() == 100


def test_deposit(bank_account):
    # Проверка депозита
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150


def test_withdraw(bank_account):
    # Проверка снятия средств
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70


def test_withdraw_insufficient_funds(bank_account):
    # Проверка снятия больше средств, чем доступно
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)


def test_deposit_negative_amount(bank_account):
    # Проверка депозита отрицательной суммы
    with pytest.raises(ValueError):
        bank_account.deposit(-10)
