from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        queue = deque([root])
        result = []
        visited = []
        while queue:
            level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                if current:
                    level.append(current.val)
                    visited.append(current.val)
                    for node in [current.left, current.right]:
                        if node:
                            queue.append(node)
            if level:
                result.append(level)

        return result

#      3
#     /  \
#    9    20
#        /  \
#       15   7


if __name__ == "__main__":
    tree_data = {
        "val": 3,
        "left": TreeNode(val=9),
        "right": TreeNode(**{
            "val": 20,
            "left": TreeNode(15),
            "right": TreeNode(7)
        })
    }
    tree = TreeNode(**tree_data)
    sol = Solution()
    
    print(sol.levelOrder(tree))
