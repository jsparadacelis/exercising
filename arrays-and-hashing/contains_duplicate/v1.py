from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1]:
                return True
        return False
