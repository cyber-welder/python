"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def int_func(s):
    return s.capitalize()


print(int_func('строка'))
