
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

array = 'a a a b c a a d c d d'
array = array.split(' ')
result = ' '

for i in array:
    count0 = str(result.count(i))
    if result.count(i) == 0:
        result +=i + ' '
    else: result += i + '_' + count0 + ' '
print(result)

# data = input("Enter your list: ").split()
#
# freequence_dict = {}
#
# for char in data:
#     if char not in freequence_dict:
#         freequence_dict[char] = 1
#         print(char, end=' ')
#     else:
#         print(f'{char}_{freequence_dict[char]}', end=' ')
#         freequence_dict[char] += 1

# data = input("Enter your list: ").split()
# dict_counter = {}
#
# for char in data:
#     print(f'{char}_{dict_counter.get(char)}' if char in dict_counter else char, end=' ')
#     dict_counter[char] = dict_counter.get(char, 0) + 1