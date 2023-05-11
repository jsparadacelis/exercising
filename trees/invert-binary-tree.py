from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':

    tree = {
        "val": 4,
        "left": TreeNode(**{
            "val": 2,
            "left": TreeNode(1),
            "right": TreeNode(3)
        }),
        "right": TreeNode(**{
            "val": 7,
            "left": TreeNode(6),
            "right": TreeNode(9)
        })
    }
    tree = TreeNode(**tree)
    sol = Solution()
    sol.invertTree(tree)
