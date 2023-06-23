from typing import List

TEST_CASES = [
    {
        "input": {
            "height": [0,1,0,2,1,0,1,3,2,1,2,1]
        },
        "result": 6
    },
    {
        "input": {
            "height": [4,2,0,3,2,5]
        },
        "result": 9
    }
]

class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0

        trapped_water = 0

        # pointers
        left = 0
        right = len(height) - 1

        # max
        max_left = height[left]
        max_right = height[right]


        while left <= right:

            if max_left <= max_right:
                diff = max_left - height[left]
                if diff > 0:
                    trapped_water += diff
                max_left = max(max_left, height[left])
                left += 1
            else:
                diff = max_right - height[right]
                if diff > 0:
                    trapped_water += diff
                max_right = max(max_right, height[right])
                right -= 1


        return trapped_water


if __name__ == '__main__':

    solution = Solution()
    
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.trap(**input)
        assert result == expected
