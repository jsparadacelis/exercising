from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 1. looking for the right row
        top = 0
        bottom = len(matrix) - 1


        while top <= bottom:

            row = (top + bottom)//2
            
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l+r)//2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False


if __name__ == '__main__':

    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 1
    print(sol.searchMatrix(matrix, target))