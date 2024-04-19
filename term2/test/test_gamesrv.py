import unittest
from gamesrv import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        latency('gamesrv_1.in.txt',
             'gamesrv_1.out.txt')
        file = open('gamesrv_1.out.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 100)

    def test_2(self):
        latency('gamesrv_2.in.txt',
             'gamesrv_2.out.txt')
        file = open('gamesrv_2.out.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10)

    def test_3(self):
        latency('gamesrv_3.in.txt',
             'gamesrv_3.out.txt')
        file = open('gamesrv_3.out.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 1000000000)

    def test_4(self):
        latency('gamesrv_4.in.txt',
             'gamesrv_4.out.txt')
        file = open('gamesrv_4.out.txt', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, 'None')


if __name__ == '__main__':
    unittest.main()
