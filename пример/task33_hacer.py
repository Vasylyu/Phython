
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_journal(lst):
    maxim = 0
    minim = float('inf')
    for i in lst:
        if minim > i:
           minim = i
        if maxim < i:
           maxim = i
    print("max", maxim, "min", minim)
    for i in range(len(lst)):
        if lst[i] == maxim:
            lst[i] = minim
    return lst

journal = [2, 3, 9, 3, 4, 7]

print(change_journal(journal))

# def change_journal(lst):
#     maximum=0
#     minimum=float('inf')
#     for i in lst:
#         if maximum < i:
#             maximum = i
#         if minimum > i:
#             minimum = i
#     print("max",maximum,"min",minimum)
#     for i in range(len(lst)):
#         if lst[i] == maximum:
#             lst[i] = minimum
#     return lst
#
#
# journal = [-1, 3, 1616516165, 3, 4]
#
#
# print(change_journal(journal))