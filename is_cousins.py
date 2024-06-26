class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def isSibling(root, a , b):
	if root is None:
		return 0

	return ((root.left == a and root.right ==b) or
			(root.left == b and root.right == a)or
			isSibling(root.left, a, b) or
			isSibling(root.right, a, b))

def level(root, val, lev):
	if root is None :
		return 0
	if root == val: 
		return lev

	l = level(root.left, val, lev+1)
	if l != 0:
		return l
	return level(root.right, val, lev+1)


def isCousin(root,a, b):
	if ((level(root,a,1) == level(root, b, 1)) and
			not (isSibling(root, a, b))):
		return True
	else:
		return False


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

node1 = root.left.right
node2 = root.right.right 

print ("Yes" if isCousin(root, node1, node2) == 1 else "No")
