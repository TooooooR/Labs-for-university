import unittest
from lan_to_venice import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        result = read_file('data_1.csv')
        self.assertEqual(result, 110)

    def test_2(self):
        result = read_file('data_2.csv')
        self.assertEqual(result, 10)

    def test_3(self):
        result = read_file('data_3.csv')
        self.assertEqual(result, 12)

    def test_4(self):
        result = read_file('data_4.csv')
        self.assertEqual(result, 4)

    def test_5(self):
        result = read_file('data_5.csv')
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
