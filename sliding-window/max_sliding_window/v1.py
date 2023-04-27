from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        for left in range(len(nums)-k+1):
            right = left
            
            while (right - left) < k:
                max_win = nums[right]
                if max_win < nums[right]:
                    max_win = nums[right]
                right += 1
            res.append(max_win)
        return res
           

if __name__ == "__main__":

    sol = Solution()
    nums = [1]
    k = 1
    print(sol.maxSlidingWindow(nums, k))