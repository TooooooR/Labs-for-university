import unittest
from rabin_karp import *


class TestFiniteAutomata(unittest.TestCase):
    def test_1(self):
        result = rabin_karp("aaaacabaabcadacab", "acab")
        self.assertEqual(result, [3, 13])

    def test_2(self):
        result = rabin_karp("asdghjasdasdeerasd", "asd")
        self.assertEqual(result, [0, 6, 9, 15])

    def test_3(self):
        result = rabin_karp("aabaacaadaabaaabaa", "aaba")
        self.assertEqual(result, [0, 9, 13])

    def test_4(self):
        result = rabin_karp("cdcdiiooaadaaaafff", "nnn")
        self.assertEqual(result, [])

    def test_5(self):
        result = rabin_karp("", "")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
