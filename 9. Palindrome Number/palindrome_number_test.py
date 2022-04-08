import unittest

from palindrome_number import Solution


class PalindromeNumberTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            Solution.isPalindrome(
                self=None,
                x=121
            ),
            True
        )

    
    def test_two(self):
        self.assertEqual(
            Solution.isPalindrome(
                self=None,
                x=-121
            ),
            False
        )

    def test_three(self):
        self.assertEqual(
            Solution.isPalindrome(
                self=None,
                x=10
            ),
            False
        )