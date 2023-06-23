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

        max_lefts = []
        max_left = 0
        trapped_water = 0
        for i in range(len(height)):
            max_lefts.append(max_left)
            max_left = max(max_left, height[i])
        
        max_rights = []
        max_right = 0
        for i in range(len(height)-1, -1, -1):
            max_rights.append(max_right)
            max_right = max(max_right, height[i])

        max_rights = max_rights[::-1]
        for i in range(len(height)):

            max_i_left = max_lefts[i]
            max_i_right = max_rights[i]
            current_height = height[i]
            diff = min(max_i_left, max_i_right) - current_height
            if diff > 0:
                trapped_water += diff

        return trapped_water


if __name__ == '__main__':

    solution = Solution()
    
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.trap(**input)
        assert result == expected
