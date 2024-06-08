class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def IsFoldable(root):
	if (root == None):
		return True
	return IsFoldableUtil(root.left, root.right)

def IsFoldableUtil(n1, n2):
	if n1 == None and n2 == None:
		return True

	if n1 == None or n2 == None:
		return False

	d1 = IsFoldableUtil(n1.left, n2.right)
	d2 = IsFoldableUtil(n1.right, n2.left)
	return d1 and d2


# Driver code
if __name__ == "__main__":

	""" The constructed binary tree is 
	1 
	/ \ 
	2 3 
	\ / 
	4 5 
"""
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.right = newNode(4)
	root.right.left = newNode(5)

	if IsFoldable(root):
		print("tree is foldable")
	else:
		print("tree is not foldable")

# This code is contributed by
# Anupam Baranwal(anupambaranwal)
