import unittest
from humster import find_max_hamsters


class TestOfHumsters(unittest.TestCase):
    def test_1(self):
        s = 7
        humster = [[1, 2],
                   [2, 2],
                   [3, 1]]

        expected_result = 2
        self.assertEqual(find_max_hamsters(s, humster), expected_result)

    def test_2(self):
        s = 19
        humster = [[5, 0],
                   [2, 2],
                   [1, 4],
                   [5, 1]]

        expected_result = 3
        self.assertEqual(find_max_hamsters(s, humster), expected_result)

    def test_3(self):
        s = 2
        humster = [[1, 50000],
                   [1, 60000]]

        expected_result = 1
        self.assertEqual(find_max_hamsters(s, humster), expected_result)
