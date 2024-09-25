import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    # Получаем список файлов в текущей директории
    files = os.listdir('test_folder')

    # Фильтруем только нужные файлы с указанным расширением
    filtered_files = [file for file in files if file.endswith(source_ext)]

    # Сортируем файлы по имени
    filtered_files.sort()

    # Задаем начальный номер для порядкового номера
    num = 1

    # Переименовываем файлы
    for file in filtered_files:
        # Получаем имя файла без расширения
        name = os.path.splitext(file)[0]

        # Если задан диапазон, обрезаем имя файла
        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        # Переименовываем файл
        path_old = os.path.join(os.getcwd(), folder_name, file)
        path_new = os.path.join(os.getcwd(), folder_name, new_name)
        os.rename(path_old, path_new)

        # Увеличиваем порядковый номер
        num += 1

import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
for i in range(1,5):

    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()




import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    # Получаем список файлов в текущей директории
    files = os.listdir('test_folder')

    # Фильтруем только нужные файлы с указанным расширением
    filtered_files = [file for file in files if file.endswith(source_ext)]

    # Сортируем файлы по имени
    filtered_files.sort()

    # Задаем начальный номер для порядкового номера
    num = 1

    # Переименовываем файлы
    for file in filtered_files:
        # Получаем имя файла без расширения
        name = os.path.splitext(file)[0]

        # Если задан диапазон, обрезаем имя файла
        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        # Переименовываем файл
        path_old = os.path.join(os.getcwd(), folder_name, file)
        path_new = os.path.join(os.getcwd(), folder_name, new_name)
        os.rename(path_old, path_new)

        # Увеличиваем порядковый номер
        num += 1








#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")


rename_files(desired_name="file_", num_digits=2, source_ext="txt", target_ext="txt")

folder_content = ""
files = os.listdir(folder_path)
files.sort()
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)