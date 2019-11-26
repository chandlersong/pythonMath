import unittest
from unittest import TestCase

import tools as t
import tools.utils as tools


class TestAccumulator(TestCase):

    def test_work_correct(self):
        accumulator = tools.Accumulator()
        for num in range(1, 11):
            accumulator.add_value(num)

        print(accumulator.mean())
        print(accumulator)


class TestStopWatch(TestCase):
    def test_work(self):
        stop_watch = t.create_stop_watch()

        print(stop_watch.elapse_time())
        print(stop_watch)


if __name__ == '__main__':
    unittest.main()
