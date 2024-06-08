class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    
    stack = []
    stack.append(root.left)
    stack.append(root.right)
    
    while stack:
        node1 = stack.pop()
        node2 = stack.pop()
        
        if not node1 and not node2:
            continue
        
        if not node1 or not node2 or node1.key != node2.key:
            return False
        
        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)
    
    return True

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

if isSymmetric(root):
    print("Symmetric")
else:
    print("Not symmetric")