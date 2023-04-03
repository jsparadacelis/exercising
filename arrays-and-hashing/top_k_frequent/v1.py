from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = {}
        for num in set(nums):
            result[num] = nums.count(num)

        return [k for k, _ in sorted(result.items(), key = lambda v: v[1], reverse=True)][:k]
