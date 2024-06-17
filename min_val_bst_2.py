from typing import List
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def insert(node: Node, data: int) -> Node:
	if not node:
		return Node(data)
	if data <= node.data:
		node.left = insert(node.left, data)
	else:
		node.right = insert(node.right, data)
	return node


def inorder(node: Node, sorted_inorder: List[int]) -> None:
	if not node:
		return
	inorder(node.left, sorted_inorder)
	sorted_inorder.append(node.data)
	inorder(node.right, sorted_inorder)


if __name__ == '__main__':
	root = None
	root = insert(root, 4)
	insert(root, 2)
	insert(root, 1)
	insert(root, 3)
	insert(root, 6)
	insert(root, 4)
	insert(root, 5)

	sorted_inorder = []
	inorder(root, sorted_inorder) 
	print(f"Minimum value in BST is {sorted_inorder[0]}")
