from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        arr = []
        window_size = float("inf")
        for i in range(len(nums)):

            while sum(arr) < target:
                arr.append(nums[i])
                i += 1
            
            if sum(arr) >= target:
                window_size = min(window_size, len(arr))
                arr.pop(0)
                
        
        return window_size if window_size != float("inf") else 0


if __name__ == '__main__':
    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    solution.minSubArrayLen(target=target, nums=nums)
