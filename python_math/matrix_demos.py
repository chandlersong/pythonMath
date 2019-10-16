import unittest
from unittest import TestCase

import numpy as np
from numpy.linalg import matrix_rank
from scipy import linalg as la
import scipy
from sympy import *


class MatrixCalculate(TestCase):
    def test_calculate(self):
        matrix_a = np.zeros([3, 3], np.int)
        matrix_a[0][1] = 1

        matrix_b = np.arange(start=1, stop=10).reshape([3, 3])

        print(matrix_a)
        print(matrix_b)
        print(np.dot(matrix_a, matrix_b))
        self.assertEqual(True, True)

    def test_inverse(self):
        matrix = np.random.random(9).reshape([3, 3])
        inverse = np.linalg.inv(matrix)

        print(matrix)
        print(inverse)
        dot = matrix.dot(inverse)
        print(dot)
        self.assertEqual(True, True)

    def test_lu(self):
        matrix = np.array([[9, 8, 7], [5, 6, 4], [3, 2, 1]])

        p, l, u = la.lu(matrix)

        print(p)
        print(l)
        print(u)
        self.assertEqual(True, True)

    def test_rref(self):
        matrix = np.array([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
        print(matrix_rank(matrix))
        A = Matrix(matrix)
        print(A.rref())
        print("null space: \n")
        null_space = A.nullspace()
        print(null_space)
        self.assertEqual(True, True)

    def test_null_space_2(self):
        matrix = np.array([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
        A = Matrix(matrix)
        print("null space: \n")
        null_space = A.nullspace()
        print(null_space)

        print(np.dot(matrix, np.array([-2, 1, 0, 0])))
        print(np.dot(matrix, np.array([2, 0, -2, 1])))

    def test_null_space(self):
        """
        this is not accuracy
        :return:
        """
        matrix = np.array([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
        space = la.null_space(matrix)
        print(space)
        print(space[:, 0:1])
        print(space[:, 1:2])
        print(np.dot(matrix, space[:, 0:1]))
        print(np.dot(matrix, space[:, 1:2]))
        self.assertEqual(True, True)

    def test_add_new_column(self):
        matrix = np.array([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
        print(matrix)
        column = np.array([[1], [2], [3]])
        print(column)
        print(np.hstack((matrix, column)))
        self.assertEqual(True, True)

    def test_solve_matrix(self):
        A = np.array([[1, 2, 2, 2], [2, 4, 6, 8], [3, 6, 8, 10]])
        print(A)
        b = np.array([1, 5, 6]).reshape([3, 1])
        print(b)
        print("solve")
        print(np.linalg.lstsq(A, b))

        '''
        it must be a square matrix
        '''
        ##print(scipy.linalg.solve(A, b))

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
