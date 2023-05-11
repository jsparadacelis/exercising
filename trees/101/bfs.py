class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(tree: TreeNode):

    queue = [tree] # [4]
    visited = []
    while queue:

        current = queue.pop(0) # q[], q[7], q[1, 3]
        visited.append(current.val) # v[4], v[4, 2], v[4, 2, 7]

        for node in [current.left, current.right]:
            if node:
                queue.append(node) #q[2,7], q[7, 1, 3], q[1, 3, 6, 9]
    return visited

#      4
#     /  \
#    2    7
#   /  \ /  \
#   1  3 6   9


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
    print(bfs(tree))
