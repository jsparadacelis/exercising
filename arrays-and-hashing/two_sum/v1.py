from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cont = 0
        diffs = {}
        while cont < len(nums):
            
            curr_num = nums[cont]
            if curr_num in diffs:
                return cont, diffs[curr_num]
            
            diff = target - curr_num
            diffs[diff] = cont
            cont +=1
