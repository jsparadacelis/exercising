from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 0


        return [k for k, _ in sorted(result.items(), key = lambda v: v[1], reverse=True)][:k]
