class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def printLeftBoundary(root):
    if not root:
        return
    while root:
        if root.left or root.right:
            print(root.data, end=" ")
        if root.left:
            root = root.left
        else:
            root = root.right

def printRightBoundary(root):
    if not root:
        return
    while root:
        if root.left or root.right:
            print(root.data, end=" ")
        if root.right:
            root = root.right
        else:
            root = root.left

def printLeaves(root):
    if not root:
        return
    printLeaves(root.left)
    if not root.left and not root.right:
        print(root.data, end=" ")
    printLeaves(root.right)

def printBoundary(root):
    if not root:
        return
    print(root.data, end=" ")
    printLeftBoundary(root.left)
    printLeaves(root.left)
    printLeaves(root.right)
    printRightBoundary(root.right)


# Driver code
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    printBoundary(root)