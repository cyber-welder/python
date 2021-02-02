"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

from random import randint

matrix_list1 = [[randint(10, 49) for _ in range(3)] for _ in range(3)]
matrix_list2 = [[randint(10, 49) for _ in range(3)] for _ in range(3)]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for line in self.matrix:
            for i in line:
                result += str(i) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) * len(self.matrix[0]) == len(other.matrix) * len(other.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    self.matrix[i][j] += other.matrix[i][j]
            return self
        else:
            return f'В задании не указана возможность сложения матриц разных размеров )))'

table1 = Matrix(matrix_list1)
table2 = Matrix(matrix_list2)

print('Матрица 1')
print(table1)
print('Матрица 2')
print(table2)
table3 = table1 + table2
print('Сумма')
print(table3)
