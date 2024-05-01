from src.pumpkins import find_robot_way
import unittest


class TestOfRobotsWays(unittest.TestCase):

    def test_1(self):
        """
        Поле розміром m==n==5
        """
        field_with_pumpkins_1 = [[1, 2, 3, 4, 5],
                                 [6, 7, 8, 9, 10],
                                 [11, 12, 13, 14, 15],
                                 [16, 17, 18, 19, 20],
                                 [21, 22, 23, 24, 25]]

        expected_result = [25, 20, 15, 10, 5, 4, 9, 14, 19, 24, 23, 18, 13, 8, 3, 2, 7, 12, 17, 22, 21, 16, 11, 6, 1]
        self.assertEqual(find_robot_way(field_with_pumpkins_1), expected_result)

    def test_2(self):
        """
        Поле розміром m = 2, n = 4
        """
        field_with_pumpkins_2 = [[1, 2, 3, 4],
                                 [5, 6, 7, 8]]

        expected_result = [8, 4, 3, 7, 6, 2, 1, 5]
        self.assertEqual(find_robot_way(field_with_pumpkins_2), expected_result)

    def test_3(self):
        """
        Поле розміром n = 1, m = 6
        """
        field_with_pumpkins_3 = [[1],
                                 [7],
                                 [11],
                                 [16],
                                 [1],
                                 [12]]

        expected_result = [12, 1, 16, 11, 7, 1]
        self.assertEqual(find_robot_way(field_with_pumpkins_3), expected_result)
