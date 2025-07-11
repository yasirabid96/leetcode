# Two sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, num in enumerate(nums):
            difference = target - nums[index]
            if difference in result:
                return [result[difference], index]
            else:
                result[num] = index


s = Solution()
print(s.twoSum([5, 4, 3, 2, 1], 8))
