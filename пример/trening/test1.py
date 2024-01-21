
# Учитывая строку, вы должны вернуть строку,
# в которой каждый символ (с учетом регистра) повторяется один раз.
# def double_char(s):
#     a = ""
#     for i in s:
#         a += i * 2
#     return a
# print(double_char('string'))
def double_char(s):
    return ''.join([i+i for i in s])
print(double_char('string'))