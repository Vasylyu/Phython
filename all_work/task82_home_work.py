# Объединение данных из нескольких JSON файлов
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json,
# employees3.json. Нужно объединить их в один файл all_employees.json.

import json
import glob
def merge_json_files(input_files, output_file):
    """Объединяет данные из нескольких JSON файлов в один."""
    merged_data = [] # Список для хранения объединенных данных
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f) # Чтение данных из файла
                merged_data.extend(data) # Добавление данных в общий список
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON файла: {file}")
    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4)

if __name__ == "__main__":
        # Получаем все JSON файлы в текущей директории
    json_files = glob.glob('task8_2.json')
    merge_json_files(json_files, 'all_employees.json')