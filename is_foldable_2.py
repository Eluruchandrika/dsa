class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def isFoldable(root):
	q = []
	if root != None:
		q.append(root.left)
		q.append(root.right)

	while (len(q) != 0):
		p = q.pop(0)
		r = q.pop(0)

		if (p == None and r == None):
			continue
		if ((p == None and r != None) or (p != None and r == None)):
			return False
		q.append(p.left)
		q.append(r.right)
		q.append(p.right)
		q.append(r.left)
	return True


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.left.right = Node(5)

if isFoldable(root):
	print("tree is foldable")
else:
	print("tree is not foldable")

