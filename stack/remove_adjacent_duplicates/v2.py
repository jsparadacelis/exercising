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

        result = ""
        for letter in s:
            if not result or result[-1] != letter:
                result += letter
            elif result[-1] == letter:
                result = result[:-1]
        return result

if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.removeDuplicates(**input)
        assert result == expected
