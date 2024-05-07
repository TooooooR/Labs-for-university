import unittest
from src.lan_to_venice import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        floyd_matrix = read_file('./resources/data_for_venice/data_1.csv')
        result = count_sum(floyd_matrix)
        self.assertEqual(result, 442)

    def test_2(self):
        floyd_matrix = read_file('./resources/data_for_venice/data_2.csv')
        result = count_sum(floyd_matrix)
        self.assertEqual(result, 68)

    def test_3(self):
        floyd_matrix = read_file('./resources/data_for_venice/data_3.csv')
        result = count_sum(floyd_matrix)
        self.assertEqual(result, 112)

    def test_4(self):
        floyd_matrix = read_file('./resources/data_for_venice/data_4.csv')
        result = count_sum(floyd_matrix)
        self.assertEqual(result, 15)

    def test_5(self):
        result = read_file('./resources/data_for_venice/data_5.csv')
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
