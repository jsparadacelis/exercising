class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()
        for i in range(len(nums)):

            num = nums[i]
            if i > 0 and num == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                
                add = num + nums[left] + nums[right]
                if add < 0:
                    left += 1
                elif add > 0:
                    right -= 1
                else:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
        return result