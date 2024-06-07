class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

def isMirrored(root1, root2):
	if root1 is None and root2 is None:
		return True

	if root1 is None or root2 is None:
		return False

	stack1 = []
	stack2 = []
	stack1.append(root1)
	stack2.append(root2)

	while stack1 and stack2:
		curr1 = stack1.pop()
		curr2 = stack2.pop()

		if curr1.data != curr2.data:
			return False

		if curr1.left is not None and curr2.right is not None:
			stack1.append(curr1.left)
			stack2.append(curr2.right)
		elif curr1.left is not None or curr2.right is not None:
			return False

		if curr1.right is not None and curr2.left is not None:
			stack1.append(curr1.right)
			stack2.append(curr2.left)
		elif curr1.right is not None or curr2.left is not None:
			return False

	if stack1 or stack2:
		return False
	return True

# create the two trees
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

if isMirrored(root1, root2):
	print("Yes")
else:
	print("No")
