from typing import List

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        # we know that the max in piles will work
        min_bananas_per_hour = right
        while left <= right:
            k_candidate = (right + left)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/k_candidate)
            
            if total <= h:
                # update minimum bananas
                min_bananas_per_hour = min(min_bananas_per_hour, k_candidate)
                right = k_candidate - 1
            elif total > h:
                left = k_candidate + 1
        return min_bananas_per_hour


if __name__ == '__main__':
    sol = Solution()
    piles = [30,11,23,4,20]
    h = 6
    print(sol.minEatingSpeed(piles=piles, h=h))
