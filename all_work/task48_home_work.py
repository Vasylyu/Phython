# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:

#file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
#
# ('C:/Users/User/Documents/', 'example', '.txt')

import os
file_path = "C:/Users/User/Documents/example.txt"
def parse_path(file_path):
    filepath, file_extension = os.path.splitext(file_path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)
print(parse_path(file_path))

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)
print(get_file_info(file_path))
# file_path1 = tuple(file_path)
# count = 0
# for i in file_path1:
#     if i == "/":
#         count += 1
# print(count, file_path1)
# count = file_path1.count('User')
# print(file_path1, count)
