
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      # we don't want to let i get to the last value in the list
      for i in range(len(nums) - 1):

        # this number is what needs to be in nums for i to work
        compliment_value = target - nums[i]

        compliment_value_slice = nums[i+1:]

        # we found the solution
        # this being true is guaranteed, so no error case is necessary
        if compliment_value in compliment_value_slice:

          # this is done to prevent using the same index as i
          compliment_index = compliment_value_slice.index(compliment_value) + i + 1

          return [i, nums[i+1:].index(compliment_value) + i + 1]

