from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        visited = {}

        for row in range(9):
            for col in range(9):
                
                value = board[row][col]
                if value == ".":
                    continue
                
                if row not in visited:
                    visited[row] = {f"row-{value}"}
                elif f"row-{value}" in visited[row]:
                    return False
                else:
                    visited[row].add(f"row-{value}")
                
                if col not in visited:
                    visited[col] = {f"column-{value}"}
                elif f"column-{value}" in visited[col]:
                    return False
                else:
                    visited[col].add(f"column-{value}")
                
                # interpret each 3x3 box as a pair (key, value) where value are all 9 values
                if (row//3, col//3) not in visited:
                    visited[row//3, col//3] = {value}
                elif value in visited[row//3, col//3]:
                    return False
                else:
                    visited[row//3, col//3].add(value)
        return True
