import unittest
from unittest import TestCase

from matplotlib import pyplot as plt


def f1(x):
    if x != 2:
        return 2 * (x ** 2) / (x - 2)


class TestDrawFunction(TestCase):

    def test_draw_f1_function(self):
        x = list(range(-11, 11))
        x.append(1.9)
        x.append(1.99)
        x.append(2.01)
        x.append(2.1)
        x.sort()
        y = [f1(i) for i in x]

        plt.xlabel('x')
        plt.ylabel('f1(x)')
        plt.grid()
        plt.plot(x, y, color='lightgrey', marker='o', markeredgecolor='green', markerfacecolor='green')
        plt.show()


if __name__ == '__main__':
    unittest.main()
