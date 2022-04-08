class Solution:
    def isPalindrome(self, x: int) -> bool:

        # solving with converting to a string
        reversed_x = list(str(x))
        reversed_x.reverse()

        return str(x) == ''.join(reversed_x)
