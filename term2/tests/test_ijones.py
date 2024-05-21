import unittest
from src.ijones import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        read_file('./resources/data_for_ijones/ijones.in_1.txt', './resources/data_for_ijones/ijones.out_1.txt')
        with open('./resources/data_for_ijones/ijones.out_1.txt', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, 5)

    def test_2(self):
        read_file('./resources/data_for_ijones/ijones.in_2.txt', './resources/data_for_ijones/ijones.out_2.txt')
        with open('./resources/data_for_ijones/ijones.out_2.txt', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, 2)

    def test_3(self):
        read_file('./resources/data_for_ijones/ijones.in_3.txt', './resources/data_for_ijones/ijones.out_3.txt')
        with open('./resources/data_for_ijones/ijones.out_3.txt', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, 201684)


if __name__ == '__main__':
    unittest.main()
