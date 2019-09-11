import unittest
from unittest import TestCase

import numpy as np


class MatrixCalculate(TestCase):
    def test_calculate(self):
        matrix_a = np.zeros([3, 3], np.int)
        matrix_a[0][1] = 1

        matrix_b = np.arange(start=1, stop=10).reshape([3, 3])

        print(matrix_a)
        print(matrix_b)
        print(np.dot(matrix_a, matrix_b))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
