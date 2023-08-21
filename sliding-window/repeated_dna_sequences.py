from typing import List

TEST_CASES = [
    {
        "input": {
            "s": "AAAAAAAAAAAAA"
        },
        "expected": ["AAAAAAAAAA"]
    },
    {
        "input": {
            "s": "AAAAAAAAAAA",
        },
        "expected": ["AAAAAAAAAA"]
    }
]

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        if len(s) == 10:
            return s

        seen = {}
        output = []
        for left in range(len(s) - 10 + 1):

            right = left + 10
            sequence = s[left:right]
            # looking for a string in set is faster
            if sequence not in seen:
                seen[sequence] = 1
            elif seen[sequence] == 1:
                output.append(sequence)
                seen[sequence] += 1
            else:
                continue

        return output


if __name__ == '__main__':

    for case in TEST_CASES:
        solution = Solution()
        result = solution.findRepeatedDnaSequences(**case["input"])
        assert result == case["expected"]
        