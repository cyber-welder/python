"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# не понял как точно реализовать ввод данных, сделал так:
n = list(input('Ведите список элементов (через пробел): ').split())
print(n)
for i in range(0, len(n)-1, 2):
    n[i], n[i + 1] = n[i + 1], n[i]
print(n)
