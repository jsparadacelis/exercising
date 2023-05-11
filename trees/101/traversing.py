class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order(tree: TreeNode):

    if tree.left:
        in_order(tree.left)

    print(tree.val)

    if tree.right:
        in_order(tree.right)


def pre_order(tree: TreeNode):

    print(tree.val)

    if tree.left:
        pre_order(tree.left)
    
    if tree.right:
        pre_order(tree.right)


def post_order(tree: TreeNode):

    if tree.left:
        pre_order(tree.left)
    
    if tree.right:
        pre_order(tree.right)
    
    print(tree.val)



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
    post_order(tree)
