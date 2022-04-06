import unittest

from solution import Solution


class TwoSumTest(unittest.TestCase):
  def test_one(self):
    self.assertEqual( 
      Solution.twoSum(
        self=None,
        nums=[2, 7, 11, 15],
        target=9
      ),
      [0, 1]
    )


  def test_two(self):
    self.assertEqual( 
      Solution.twoSum(
        self=None,
        nums=[3, 2, 4],
        target=6
      ),
      [1, 2]
    )

  def test_three(self):
    self.assertEqual( 
      Solution.twoSum(
        self=None,
        nums=[3, 3],
        target=6
      ),
      [0, 1]
    )



if __name__ == "__main__":
  unittest.main()