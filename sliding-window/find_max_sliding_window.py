from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        dq = deque()
        start = 0
        end = 0

        while end < len(nums):

            # if que have data in dq and the last element
            # is less than incoming one, lets pop and then
            # add the incoming one
            while dq and nums[dq[-1]] < nums[end]:
                dq.pop()
            dq.append(end)
            
            # if first value at dq is less than left or start pointer
            # lets remove this first value cause
            # doesn't make sense to consider it
            if start > dq[0]:
                dq.popleft()

            # if window size is k, lets append the first value from dq
            if (end - start + 1) >= k:
                result.append(nums[dq[0]])
                start += 1 
            end += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,1,2,0,5]
    # [3,3,2,5]
    k = 3
    solution.maxSlidingWindow(nums=nums, k=k)
