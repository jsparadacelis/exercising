from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:
            return 1
        
        lv = self.maxDepth(root.left)
        rv = self.maxDepth(root.right)
        return max(lv, rv) + 1


if __name__ == '__main__':

    tree = {
        "val": 3,
        "left": TreeNode(9),
        "right": TreeNode(**{
            "val": 20,
            "left": TreeNode(15),
            "right": TreeNode(7)
        })
    }
    tree = TreeNode(**tree)
    sol = Solution()
    print(sol.maxDepth(tree))
