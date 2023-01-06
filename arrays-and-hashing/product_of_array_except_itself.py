from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        product = 1

        for idx, number in enumerate(nums):
            result[idx] = product
            product *= number

        product = 1
        for idx, number in enumerate(nums[::-1], start=1):
            result[-idx] *= product
            product *= number

        return result
