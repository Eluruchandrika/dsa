class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def preorder(root, v):
    if root == None:
        return
    v.append(root.data)
    if root.left:
        preorder(root.left, v)
    else:
        v.append(0)
    if root.right:
        preorder(root.right, v)
    else:
        v.append(0)

def isIdentical(root1, root2):
    v = []
    x = []
    preorder(root1, v)
    preorder(root2, x)
    return v == x

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if isIdentical(root1, root2):
    print("Both the trees are identical.")
else:
    print("Given trees are not identical.")