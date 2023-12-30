
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# a = [1,1,2,0,-1,3,4,4]
# count = set(a)
# print(len(count))

lst = [1,1,2,0,-1,3,4,4]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(len(lst1), '\n', lst1)