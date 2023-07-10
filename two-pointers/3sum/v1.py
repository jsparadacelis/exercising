from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = []
        for i in range(len(nums)):

            num = nums[i]
            if i > 0 and num == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_up = num + nums[left] + nums[right]

                if sum_up > 0:
                    right -= 1
                elif sum_up < 0:
                    left += 1
                else:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return triplets


if __name__ == '__main__':

    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    sol.threeSum(nums=nums)
