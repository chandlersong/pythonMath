import unittest
from unittest import TestCase

import tools.utils as tools

class TestAccumulator(TestCase):

    def test_work_correct(self):
        accumulator = tools.Accumulator()
        for num in range(1,11):
            accumulator.add_value(num)

        print(accumulator.mean())
        print(accumulator)
            


class TestTimer(TestCase):
    pass

if __name__ == '__main__':
    unittest.main()