from typing import List


TEST_CASES = [
    {
        "input": {
            "matrix": [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            "target": 3
        },
        "result": True
    },
    {
        "input": {
            "matrix": [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            "target": 13
        },
        "result": False
    },
]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # 1. Determine in which sub-array target could be located

        left = 0
        right = len(matrix) - 1
        candidate = []
        while left <= right:

            mid = (left + right)//2
            sub_array = matrix[mid]
            if sub_array[0] <= target <= sub_array[-1]:
                if target == sub_array[0] or target == sub_array[-1]:
                    return True
                candidate = sub_array
                break
            else:
                if target < sub_array[0]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        if not candidate:
            return False
        
        left = 0
        right = len(candidate) - 1
        while left <= right:
            mid = (left + right)//2
            if candidate[mid] == target:
                return True
            elif target < candidate[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.searchMatrix(**input)
        assert result == expected
