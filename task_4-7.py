"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
"""

from math import factorial


def fact(n):
    for f in range(n):
        yield factorial(f + 1)


generator = fact(9)

for el in generator:
    print(el)
