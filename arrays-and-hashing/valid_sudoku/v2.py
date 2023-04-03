from collections import defaultdict

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visited = defaultdict(set)

        for row in range(9):
            for col in range(9):
                
                value = board[row][col]
                if value == ".":
                    continue
                
                # interpret each 3x3 box as a pair (key, value) where value are all 9 values
                if f"row-{value}" in visited[row] or f"col-{value}" in visited[col] or value in visited[row//3, col//3]:
                    return False
                
                visited[row].add(f"row-{value}")
                visited[col].add(f"col-{value}")
                visited[row//3, col//3].add(value)
        return True
