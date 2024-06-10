class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(node, nodes):
    if not node:
        return
    inorder_traversal(node.left, nodes)
    nodes.append(node)
    inorder_traversal(node.right, nodes)

def build_balanced_bst(nodes, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = nodes[mid]
    
    root.left = build_balanced_bst(nodes, start, mid - 1)
    root.right = build_balanced_bst(nodes, mid + 1, end)
    
    return root

def balance_bst(root):
    nodes = []
    inorder_traversal(root, nodes)
    
    return build_balanced_bst(nodes, 0, len(nodes) - 1)


# Creating an unbalanced BST
root = TreeNode(10)
root.left = TreeNode(8)
root.left.left = TreeNode(7)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(5)

balanced_root = balance_bst(root)

def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)

print_inorder(balanced_root)
