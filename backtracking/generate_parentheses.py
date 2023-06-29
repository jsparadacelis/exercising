from typing import List


TEST_CASES = [
    {
        "input": {
            "n": 3
        },
        "result": ["((()))","(()())","(())()","()(())","()()()"]
    },
    {
        "input": {
            "n": 1
        },
        "result": ["()"]
    },
]

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        root = "("
        open_par = 1
        close_par = 0
        result = []

        def backtrack(root, open_par, close_par):
            if open_par == close_par == n:
                result.append(root)
                return
            
            if open_par < n:
                backtrack(root + "(", open_par+1, close_par)
            
            if close_par < open_par:
                backtrack(root + ")", open_par, close_par+1)
        backtrack(root, open_par, close_par)
        return result


if __name__ == '__main__':
    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.generateParenthesis(**input)
        assert result == expected
        