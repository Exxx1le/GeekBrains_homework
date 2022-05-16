# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            new_list.append([])
            for k in range(len(self.list[0])):
                new_list[i].append(self.list[i][k] + other.list[i][k])
        return Matrix(new_list)


matrix_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_list2 = [10, 11, 12], [13, 14, 15], [16, 17, 18]
matrix1 = Matrix(matrix_list1)
matrix2 = Matrix(matrix_list2)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
