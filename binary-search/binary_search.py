from typing import List

TEST_CASES = [
    {
        "input": {
            "nums": [-1,0,3,5,9,12],
            "target": 9
        },
        "result": 4
    },
    {
        "input": {
            "nums": [-1,0,3,5,9,12],
            "target": -2
        },
        "result": -1
    },
    {
        "input": {
            "nums": [5],
            "target": 5
        },
        "result": 0
    }

]


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = 0
        left = len(nums) - 1

        while right <= left:

            half = (left + right)//2
            if target > nums[half]:

                right = half+1
            elif target < nums[half]:
                left = half-1
            elif target == nums[half]:
                return half
        return -1

if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.search(**input)
        assert result == expected
