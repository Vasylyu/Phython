'''
Напишите однострочный генератор словаря, который принимает на вход
три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
Не забудьте распечатать в конце результат.

На входе:
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

На выходе:
{'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}
'''

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
summa_bonus1 = (salary[0] * float(bonus[0].strip("%"))) / 100
summa_bonus2 = (salary[1] * float(bonus[1].strip("%"))) / 100
summa_bonus3 = (salary[2] * float(bonus[2].strip("%"))) / 100
summa_bonus = [summa_bonus1, summa_bonus2, summa_bonus3]

a = {names[i]: summa_bonus[i] for i in range(len(names))}
print(summa_bonus)
print(a)


result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)

