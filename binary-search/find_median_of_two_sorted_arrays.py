from typing import List

TEST_CASES = [
    {
        "input": {
            "nums1": [2, 4, 9, 10, 16],
            "nums2": [8, 12, 19, 20, 22, 28]
        },
        "expected": 12
    },
    {
        "input": {
            "nums1": [1, 3],
            "nums2": [2]
        },
        "expected": 2
    },
    {
        "input": {
            "nums1": [1, 3],
            "nums2": [2, 4]
        },
        "expected": 2.5
    }
]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # determine the shortest array
        array_a = nums1
        array_b = nums2
        total = len(array_a) + len(array_b)
        half = total//2
        if len(nums2) < len(nums1):
            array_a, array_b = array_b, array_a # switching arrays

        left = 0
        right = len(array_a) - 1

        while True:
            
            partition_a = (left + right)//2
            # to know how many items we need from b
            # due to we start indexing at 0, we need to sum up partition_a with 1 to get
            # the right quantity of numbers to complete from array_b
            partition_b = half - (partition_a + 1) - 1

            max_left_a = array_a[partition_a] if partition_a >= 0 else float("-inf")
            max_left_b = array_b[partition_b] if partition_b >= 0 else float("-inf")

            min_right_a = array_a[partition_a + 1] if partition_a + 1 < len(array_a) else float("inf")
            min_right_b = array_b[partition_b + 1] if partition_b + 1 < len(array_b) else float("inf")


            if max_left_a > min_right_b:
                right = partition_a - 1
            elif max_left_b > min_right_a:
                left = partition_a + 1
            else:
                # odd
                if total % 2:
                    return min(min_right_a, min_right_b)
                else:
                    return (max(max_left_a, max_left_b) + min (min_right_a, min_right_b))/2

if __name__ == "__main__":

    solution = Solution()

    for test in TEST_CASES:
        result = solution.findMedianSortedArrays(**test["input"])
        assert result == test["expected"]
