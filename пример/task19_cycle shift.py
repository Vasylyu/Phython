
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# spis1 = [1,2,3,4,5]
# spis2 = []
# k = 3
# k = k % len(spis1)
# for i in range(len(spis1)):
#     if i + k > len(spis1)-1:
#         temp = i + k - len(spis1)
#         spis2.append(spis1[temp])
#     else:
#         spis2.append(spis1[i + k])
#
# print(spis2)

# lst = [1,2,3,4,5]
# lst_shift = []
# shift = 3
# for i in range(len(lst)):
#     lst_shift.append(lst[(i + shift) % len(lst)])
# print(lst_shift)

lst = [1, 2, 3, 4, 5]
k = 3
lst_shift = lst[k:] + lst[:k]
print(lst_shift)