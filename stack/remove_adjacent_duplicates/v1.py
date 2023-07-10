TEST_CASES = [
    {
        "input": {
            "s": "abbaca"
        },
        "result": "ca"
    },
    {
        "input": {
            "s": "azxxzy"
        },
        "result": "ay"
    }
]   

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = s.lower()
        for letter in s:
            if not stack or stack[-1] != letter:
                stack.append(letter)
            elif stack[-1] == letter:
                stack.pop()
        return "".join(stack)

if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.removeDuplicates(**input)
        assert result == expected
