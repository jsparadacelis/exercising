from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        right = 0
        left = len(height) - 1

        highest = 0
        while right < left:

            area = (left - right) * min(height[right], height[left])
            highest = max(highest, area)

            if height[left] > height[right]:
                right += 1
            
            elif height[left] < height[right]:
                left -= 1
            else:
                right += 1
                left -= 1

        return highest