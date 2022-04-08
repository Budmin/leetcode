import unittest

from average_salary import Solution


class AverageSalaryTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            Solution.average(
                self=None, 
                salary=[4000, 3000, 1000, 2000]
            ),
            2500.00000
        )

    def test_two(self):
        self.assertEqual(
            Solution.average(
                self=None,
                salary=[1000, 2000, 3000]
            ),
            2000.00000
        )