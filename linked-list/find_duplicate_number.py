from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return fast


if __name__ == "__main__":

    solution = Solution()
    nums = [3,1,3,4,2]
    solution.findDuplicate(nums=nums)