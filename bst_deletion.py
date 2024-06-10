class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self.minValue(root.right)
            root.right = self.deleteNode(root.right, root.key)

        return root

    def minValue(self, root):
        minv = root.key
        while root.left:
            minv = root.left.key
            root = root.left
        return minv

if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = tree.insert(tree.root, 50)
    tree.insert(tree.root, 30)
    tree.insert(tree.root, 20)
    tree.insert(tree.root, 40)
    tree.insert(tree.root, 70)
    tree.insert(tree.root, 60)
    tree.insert(tree.root, 80)

    print("Original BST:", end=" ")
    tree.inorder(tree.root)
    print()

    print("\nDelete a Leaf Node: 20")
    tree.root = tree.deleteNode(tree.root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    tree.inorder(tree.root)
    print()

    print("\nDelete Node with single child: 70")
    tree.root = tree.deleteNode(tree.root, 70)
    print("Modified BST tree after deleting single child Node:")
    tree.inorder(tree.root)
    print()

    print("\nDelete Node with both child: 50")
    tree.root = tree.deleteNode(tree.root, 50)
    print("Modified BST tree after deleting both child Node:")
    tree.inorder(tree.root)