class newNode:
	def __init__(self, k):
		self.key = k 
		self.right = self.left = None

def count_nodes(root):
    if root == None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def isPerfect(root):
    nodes = count_nodes(root)
    return nodes & (nodes+1) == 0

# Driver Code 
if __name__ == '__main__':
	root = None
	root = newNode(10) 
	root.left = newNode(20) 
	root.right = newNode(30) 

	root.left.left = newNode(40) 
	root.left.right = newNode(50) 
	root.right.left = newNode(60) 
	root.right.right = newNode(70) 

	if (isPerfect(root)): 
		print("Yes") 
	else:
		print("No")
		
