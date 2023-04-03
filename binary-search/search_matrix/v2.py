from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) -1

        if len(matrix) == 1:
            return target in matrix[0]

        while left < right:

            if target in matrix[left] or target in matrix[right]:
                return True
            
            if target > matrix[left][-1]:
                left += 1
            elif target < matrix[right][0]:
                right -=1
        return False


if __name__ == '__main__':

    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(sol.searchMatrix(matrix, target))