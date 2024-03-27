import unittest
from heap_based_priority_queue import HeapBasedPriorityQueue


class TestOfInorderTraversal(unittest.TestCase):
    def test_1(self):
        queue = HeapBasedPriorityQueue()
        queue.insert(123, 133)
        queue.insert(45, 12)
        queue.insert('ananas', 94)
        queue.insert('algoritm', 36)
        queue.insert(12, 1810)
        queue.insert('єнот', 11)

        expected_result = [12, 123, 'ananas', 45, 'algoritm', 'єнот']
        self.assertEqual(queue.current_q(), expected_result)

    def test_2(self):
        queue = HeapBasedPriorityQueue()
        queue.insert('ananas', 11)
        queue.insert(95, 11)
        queue.insert(1, 11)
        queue.insert('algoritm', 11)
        queue.insert(120, 11)
        queue.insert('єнот', 11)

        expected_result = ['ananas', 95, 1, 'algoritm', 120, 'єнот']
        self.assertEqual(queue.current_q(), expected_result)

    def test_3(self):
        queue = HeapBasedPriorityQueue()
        queue.insert(123, 17)
        queue.insert('алгоритми', 112)
        queue.insert(12, 9)
        queue.insert(44, 0)
        queue.insert(12, 21)
        queue.insert('англійська', 78)

        expected_result = 'алгоритми'
        self.assertEqual(queue.delete_root(), expected_result)
