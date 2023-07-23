from typing import List


TEST_CASES = [
    {
        "input": {
            "nums": [6,7,1,2,3,4,5],
            "target": 3
        },
        "result": 4
    },
    {
        "input": {
            "nums": [1],
            "target": 0
        },
        "result": -1
    },
    {
        "input": {
            "nums": [4,5,6,7,0,1,2],
            "target": 0
        },
        "result": 4
    },
]

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]: # this half is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1 
                else:
                    start = mid + 1 
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1 
        return -1


if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.search(**input)
        assert result == expected
