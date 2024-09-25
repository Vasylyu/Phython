"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

def funct2(txt):
    return sorted(set([ord(symbol) for symbol in txt]),reverse=True)
txt = "Сформируйте список с уникальными кодами Unicode каждого"
print(funct2(txt))

