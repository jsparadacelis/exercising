from typing import List

TEST_CASES = [
    {
        "input": {
            "heights": [2,1,5,6,2,3]
        },
        "result": 10
    },
    {
        "input": {
            "heights": [2,4]
        },
        "result": 4
    }
]

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        for i in range(len(heights)):

            height = heights[i]
            start = i
            while stack and stack[-1][1] > height:

                prev_start, prev_value = stack.pop()
                area = prev_value * (i - prev_start)
                max_area = max(max_area, area)
                start = prev_start
            
            stack.append((start, height))
        
        for height in stack:
            start, value = height
            area = value * (len(heights) - start)
            max_area = max(max_area, area)
        return max_area
    

if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.largestRectangleArea(**input)
        assert result == expected
