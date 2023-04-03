from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # calculate mid element
        mid = len(matrix)//2
        while matrix:

            if len(matrix) == 1 and target not in matrix[mid]:
                return False
            
            if target in matrix[mid]:
                return True
            # due to each element in matrix is sorted, we can ask for first
            # and last element of each inner arr
            if target < matrix[mid][0]:
                matrix = matrix[:mid]
            elif target > matrix[mid][-1]:
                matrix = matrix[mid:]
            # if any rule applies, lets define matrix as empty array
            else:
                matrix = []
            mid = len(matrix)//2
        return False

if __name__ == '__main__':

    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 100
    print(sol.searchMatrix(matrix, target))