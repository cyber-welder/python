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

    def __add__(self, add_matrix):
        # не стал реализовывать сложение матриц разных размеров, в задании нет, да и не об этом урок ))))
        result = []
        for i in range(len(self.matrix)):
            result.append([self.matrix[i][j] + add_matrix.matrix[i][j] for j in range(len(self.matrix[i]))])
        return Matrix(result)


table1 = Matrix(matrix_list1)
table2 = Matrix(matrix_list2)

print('Матрица 1')
print(table1)
print('Матрица 2')
print(table2)
table3 = table1 + table2
print('Сумма')
print(table3)
