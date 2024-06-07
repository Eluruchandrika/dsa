class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def isSumTree(node):
    if node is None or (node.left is None and node.right is None):
        return True

    if node.left is None:
        left_sum = 0
    elif node.left.left is None and node.left.right is None:
        left_sum = node.left.val
    else:
        left_sum = 2 * node.left.val

    if node.right is None:
        right_sum = 0
    elif node.right.left is None and node.right.right is None:
        right_sum = node.right.val
    else:
        right_sum = 2 * node.right.val

    return (node.val == left_sum + right_sum) and isSumTree(node.left) and isSumTree(node.right)

# Example of a Binary Tree
root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(3)

if isSumTree(root):
    print("The Binary Tree is a SumTree")
else:
    print("The Binary Tree is not a SumTree")

