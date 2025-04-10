# test_cole_algorithms.py

import unittest
from src.bigdata_cole_framework.number_algorithms import ColeAlgorithms


class TestColeAlgorithms(unittest.TestCase):

    def test_get_max_number(self):
        self.assertEqual(ColeAlgorithms.get_max_number([1, 2, 3, 4, 5]), 5)
        self.assertEqual(ColeAlgorithms.get_max_number([-10, -5, -1]), -1)
        with self.assertRaises(ValueError):
            ColeAlgorithms.get_max_number([])

    def test_get_min_number(self):
        self.assertEqual(ColeAlgorithms.get_min_number([1, 2, 3, 4, 5]), 1)
        self.assertEqual(ColeAlgorithms.get_min_number([-10, -5, -1]), -10)
        with self.assertRaises(ValueError):
            ColeAlgorithms.get_min_number([])

    def test_get_average(self):
        self.assertEqual(ColeAlgorithms.get_average([2, 4, 6]), 4.0)
        self.assertAlmostEqual(ColeAlgorithms.get_average([1, 2, 3]), 2.0)
        self.assertEqual(ColeAlgorithms.get_average([5]), 5.0)
        with self.assertRaises(ValueError):
            ColeAlgorithms.get_average([])

    def test_get_median(self):
        self.assertEqual(ColeAlgorithms.get_median([1, 2, 3]), 2)
        self.assertEqual(ColeAlgorithms.get_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(ColeAlgorithms.get_median([10]), 10)
        self.assertEqual(ColeAlgorithms.get_median([5, 1, 9]), 5)
        with self.assertRaises(ValueError):
            ColeAlgorithms.get_median([])


if __name__ == '__main__':
    unittest.main()
