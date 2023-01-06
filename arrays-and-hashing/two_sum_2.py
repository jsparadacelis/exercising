from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}
        for index, number in enumerate(nums):
            
            if number in diffs:
                return diffs[number], index
            
            diffs[target-number] = index
