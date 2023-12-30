# def create_contact():
#     pass
#     contakts = input('Введите данные контакты через ":" : ')
#     data = open('phone_book.txt', 'a', encoding='utf-8')
#     data.writelines(contakts + '\n')
#     data.close()
# create_contact()
#
#
# def change_contact():
#     data = open('phone_book.txt', 'r+', encoding='utf-8')
#     lst = data.readlines()
#     print(lst)
#     lst2 = []
#     for i in range(len(lst)):
#         lst2.append(lst[i].split(':'))
#     lst2[0][1] = input('введите новый телефон: ')
#     print(lst2)
# change_contact()


def read_contact():
    data = open('phone_book.txt', 'r+', encoding='utf-8')
    lst = data.readlines()
    print(lst)
    lst2 = []
    for i in range(len(lst)):
        lst2.append(lst[i].split(':'))

    name = input('Введите имя: ')
    for item in lst2:
        if name in item:
            print(item)
        else:
            print('Контакт не найден')
read_contact()