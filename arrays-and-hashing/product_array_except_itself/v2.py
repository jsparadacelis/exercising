from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)


if __name__ == '__main__':

    sol = Solution()
    nums = [1,2,3,4]
    sol.productExceptSelf(nums)