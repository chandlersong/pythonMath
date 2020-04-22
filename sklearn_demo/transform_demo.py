import unittest
import numpy as np
from unittest import TestCase

from sklearn.preprocessing import FunctionTransformer


def plus(X, value):
    return X + value


class TestFunctionTest(TestCase):

    def test_function_transform(self):
        transform = FunctionTransformer(plus, kw_args={"value": 2})
        transform_value = transform.transform(np.array([1, 2, 3]))
        print("transform value")
        print(transform_value)


if __name__ == '__main__':
    unittest.main()
