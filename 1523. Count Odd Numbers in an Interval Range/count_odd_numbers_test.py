import unittest

from count_odd_numbers import Solution


class CountOddNumbersTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            Solution.countOdds(self=None, low=3, high=7),
            3
        )

    def test_two(self):
        self.assertEqual(
            Solution.countOdds(self=None, low=8, high=10),
            1
        )