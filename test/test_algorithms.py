import unittest
from sort import algorithms


class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([4, 2, 1, 3], [1, 2, 3, 4]),
            ([1], [1]),
            ([], []),
            ([1, 1, 1], [1, 1, 1]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
        ]

    def test_bubble_sort(self):
        for input_arr, expected in self.test_cases:
            result = algorithms.bubble_sort(input_arr.copy())
            self.assertEqual(result, expected)

    def test_quick_sort(self):
        for input_arr, expected in self.test_cases:
            result = algorithms.quick_sort(input_arr.copy())
            self.assertEqual(result, expected)

    def test_merge_sort(self):
        for input_arr, expected in self.test_cases:
            result = algorithms.merge_sort(input_arr.copy())
            self.assertEqual(result, expected)
