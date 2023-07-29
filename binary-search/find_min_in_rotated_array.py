from typing import List


TEST_CASES = [
    {
        "input": {
            "nums": [3,4,5,1,2],
        },
        "result": 1
    },
    {
        "input": {
            "nums": [4,5,6,7,0,1,2],
        },
        "result": 0
    },
    {
        "input": {
            "nums": [11,13,15,17],
        },
        "result": 11
    },
    {
        "input": {
            "nums": [2, 1],
        },
        "result": 1
    }

]


class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if i have an array like this one [3,4,5,1,2]
        # the left part is sorted but the left one not. It means the minimum is in the left

        start = 0
        end = len(nums) - 1
        result = nums[start]
        while start <= end:
            mid = (start+end) // 2
            result = min(result, nums[mid])
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[start] <= nums[mid] and nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return result

if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.findMin(**input)
        assert result == expected