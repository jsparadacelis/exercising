from typing import List

TEST_CASES = [
    {
        "input": {
            "temperatures": [73,74,75,71,69,72,76,73]
        },
        "result": [1,1,4,2,1,1,0,0]
    },
    {
        "input": {
            "temperatures": [30,40,50,60]
        },
        "result": [1,1,1,0]
    },
    {
        "input": {
            "temperatures": [30,60,90]
        },
        "result": [1,1,0]
    }

]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [(0, temperatures[0])]

        for idx in range(1, len(temperatures)):

            while stack and temperatures[idx] > stack[-1][1]:
                top_idx, _ = stack.pop()
                result[top_idx] = (idx - top_idx)
            stack.append((idx, temperatures[idx]))
        return result


if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.dailyTemperatures(**input)
        assert result == expected
