class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def is_bst(root,min_val=float('-inf'),max_val=float('-inf')):
    if not root:
        return True
    if root.val>=max_val or root.val<=min_val:
        return False
    return is_bst(root.left,min_val,root.val) and (root.right,root.val,max_val)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if is_bst(root):
    print("The binary tree is a binary search tree.")
else:
    print("The binary tree is not a binary search tree.")
        