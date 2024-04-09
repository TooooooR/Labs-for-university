import unittest
from num_of_islands import num_of_island


class TestOfInorderTraversal(unittest.TestCase):
    def test_1(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        expected_result = 0
        self.assertEqual(num_of_island(grid), expected_result)

    # def test_2(self):
    #     grid = [
    #         [0, 1, 0, 0, 0],
    #         [1, 1, 1, 1, 0],
    #         [1, 0, 0, 0, 0],
    #         [0, 1, 0, 1, 1]
    #     ]
    #
    #     expected_result = 2
    #     self.assertEqual(num_of_island(grid), expected_result)

    def test_3(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]

        expected_result = 1
        self.assertEqual(num_of_island(grid), expected_result)

