
#  Создайте вручную список с повторяющимися элементами.
#  Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 3, 4, 5, 5, 5, 6, 9, 9, 56, 45, 68]
count_dict = {}

for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1


my_list_copy = my_list[:]
for i in range(len(my_list_copy)):
    if count_dict[my_list_copy[i]] == 2:
        my_list.remove(my_list_copy[i])
print(my_list)
print(my_list_copy)
for item in count_dict:
    if count_dict.values() == 2:
        my_list.remove(item)

# Второе решение
count = {}
for item in my_list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
new_list = [item for item in my_list if count[item] == 1]
print(new_list)
