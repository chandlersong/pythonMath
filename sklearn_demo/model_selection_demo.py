import unittest
import pandas as pd
import numpy as np
from unittest import TestCase

from sklearn.model_selection import StratifiedShuffleSplit


class TestStratifiedShuffleSplit(TestCase):
    def test_split(self):
        """
        it's base on my guess. the data is group by the y.
        :return:
        """
        data = pd.DataFrame(np.arange(12))
        y = pd.Series([1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2])
        split = StratifiedShuffleSplit(n_splits=1, test_size=0.5)
        for train_index, test_index in split.split(data, y):
            train_set = data.iloc[train_index]
            test_set = data.iloc[test_index]
            print("train set is {}".format(train_set))
            print("test set is {}".format(test_set))


if __name__ == '__main__':
    unittest.main()
