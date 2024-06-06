class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def diagonal(root):
	out = []
	node = root
	left_q = []
	while node:
		out.append(node.data)
		if node.left:
			left_q.insert(0,node.left)
		if node.right:
			node = node.right
		else:
			if len(left_q) >= 1:
				node = left_q.pop()
			else:
				node = None
	return out


# Driver Code
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

print(diagonal(root))
