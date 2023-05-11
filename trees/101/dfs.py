class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_iterative(tree: TreeNode):

    stack = []
    visited = []
    stack.insert(0, tree)
    while stack:
        current = stack.pop(0)
        visited.append(current.val)
        for node in [current.right, current.left]:
            if node:
                stack.insert(0, node)
    return visited


def dfs_recursive(tree: TreeNode):

    if tree and not tree.left and not tree.right:
        return [tree.val]
    
    left_val = dfs_recursive(tree.left)
    right_val = dfs_recursive(tree.right)
    return [tree.val, *left_val, *right_val]


if __name__ == "__main__":
    tree_data = {
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
    tree = TreeNode(**tree_data)
    print(dfs_iterative(tree))
