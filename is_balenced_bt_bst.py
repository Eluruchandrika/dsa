class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def isBalanced(root):
	if root is None:
		return True
	lh = isBalanced(root.left)
	if lh == 0:
		return 0
	rh = isBalanced(root.right)
	if rh == 0:
		return 0
	if (abs(lh - rh) > 1):
		return 0
	else:
		return max(lh, rh) + 1


# Driver code
if __name__ == '__main__':
	root = Node(10)
	root.left = Node(5)
	root.right = Node(30)
	root.right.left = Node(15)
	root.right.right = Node(20)
	if (isBalanced(root) == 0):
		print("Not Balanced")
	else:
		print("Balanced")

