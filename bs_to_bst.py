class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def extract_values_inorder(node, values):
    if node is None:
        return

    extract_values_inorder(node.left, values)
    values.append(node.val)
    extract_values_inorder(node.right, values)

def convert_to_bst(node, values, index):
    if node is None:
        return

    convert_to_bst(node.left, values, index)
    node.val = values[index]
    index += 1
    convert_to_bst(node.right, values, index)

# Example of creating a binary tree
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

values = []
extract_values_inorder(root, values)
values.sort()

index = 0
convert_to_bst(root, values, index)

print("Binary tree converted to a binary search tree.")