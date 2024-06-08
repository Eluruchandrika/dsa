class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    root_idx = inorder.index(root_val)

    root.left = build_tree(preorder, inorder[:root_idx])
    root.right = build_tree(preorder, inorder[root_idx + 1:])

    return root

def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right)+ [root.val] 

# Example usage
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]

root = build_tree(preorder, inorder)
postorder_result = postorder_traversal(root)
print(postorder_result)