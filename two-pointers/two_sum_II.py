from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = 0
        left = len(numbers) - 1

        while right < left:

            total = numbers[left] + numbers[right]

            if total == target:
                return [right+1, left+1]
            elif total < target:
                right += 1
            else:
                left -= 1
