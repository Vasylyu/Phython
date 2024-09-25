# В большой текстовой строке text подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# Слова выведите в обратном алфавитном порядке.
# Пример
# На входе:
#
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
import re
from collections import Counter

text = 'Hello world. Hello Python. Hello again.'
# text = [('hello', len(re.findall('hello', text.lower()))),
#          ('world', len(re.findall('world', text.lower())),
#          ('python', len(re.findall('python', text.lower()))),
#           ('again', len(re.findall('again', text.lower()))))
#           ]
print(text)

# другое решение

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]
print(top_words)