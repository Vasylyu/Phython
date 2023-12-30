# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
import shutil
def print_menu():
    print('1. Создать контакт')
    print('2. Сменить контакт')
    print('3. Найти контакт')
    print('4. Удалить контакт')
    print('5. Показать контакт')
    print('6. Cкопировать контакты')
    print('7. Выход')

def input_contact(file_name):
    count = count_contact(file_name)
    information = list()
    information.append(str(count))
    information.append(input('Введите имя контакта: '))
    information.append(input('Введите номер контакта: '))
    information.append(input('Введите доп. информацию: '))
    return information


def count_contact(file_name):
    with open(file_name, 'r') as fp:
        return sum([1 for lst in fp])
def create_contact(file_name):
    contact = input_contact(file_name)
    with open(file_name, 'a') as file:
        file.write(';'.join(contact) + '\n')


def show_contacts(file_name):
    with open(file_name, 'r') as file:
        for lst in file:
            print(lst, end="")

def change_contact(file_name):
    with open(file_name, 'r') as file:
        lst = file.readlines()
    for line in lst:
       print(line, end=" ")
    n = int(input('Введите индекс контакта: '))
    if 0 <= n <= len(lst):
        contact = input_contact(file_name)
        contact[0] = str(n)
        contact = ':'.join(contact) + '\n'
        lst[n] = contact
    with open(file_name, 'w') as file:
        file.writelines(lst)

def find_contact(file_name):
    name = input('Введите имя: ')
    with open(file_name, 'r') as file:
        lst = file.readlines()
    for item in lst:
        if name in item:
            print(item)
            break
    if name not in lst:
        print('Контакт не найден')
def delete_contact(file_name):
    with open(file_name, 'r') as file:
        lst = file.readlines()
    for line in lst:
        print(lst, end='')
    n = int(input('Введите индекс контакта для изменения: '))
    if 0 <= n <= len(lst):
        del lst[n]
    with open(file_name, 'w') as file:
            file.writelines(lst)
def copy_file():
    shutil.copy2('phone_book.txt','phone_book2.txt')
    copy_file()


def main():
    file_name = 'phone_book.txt'
    while True:
        print_menu()
        input_number = int(input('Выберете раздел в меню: '))
        if input_number == 1:
            create_contact(file_name)
        elif input_number == 2:
            change_contact(file_name)
        elif input_number == 3:
            find_contact(file_name)
        elif input_number == 4:
            delete_contact(file_name)
        elif input_number == 5:
            show_contacts(file_name)
        elif input_number == 6:
            copy_file()
        elif input_number == 7:
            break
        print("Справочник завершил работу")

if __name__ == "__main__":
    main()


