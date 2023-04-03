from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visited = set()

        for row in range(9):
            for col in range(9):
                
                value = board[row][col]
                if value == ".":
                    continue
                
                # interpret each 3x3 box as a pair (key, value) where value are all 9 values
                # instead of have a map with set, differentiate each col, row and box by adding meaningful strings

                conditions = [
                    f"row-{row}-{value}" in visited,
                    f"col-{col}-{value}" in visited,
                    f"box-{row//3}-{col//3}-{value}" in visited
                ]

                if any(conditions):
                    return False
                
                visited.add(f"row-{row}-{value}")
                visited.add(f"col-{col}-{value}")
                visited.add(f"box-{row//3}-{col//3}-{value}")
            
        return True