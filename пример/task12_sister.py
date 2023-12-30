
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 45 -> 22
# 506 -> 23



s = int(input('подсказка 1: '))
p = int(input('подсказка 2: '))

solutions = []
for x in range(1, 1001):
    for y in range(1, 1001):
        if s == x + y and p == x * y:
            solutions.append((min(x, y), max(x, y)))
    solutions = list(set(solutions))
for solutions in solutions:
    print(solutions[0], solutions[1])