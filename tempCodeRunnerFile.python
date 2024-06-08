class newnode: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None
def subtreeSum(root):
    if root is None:
        return 0
    left_sum = subtreeSum(root.left)
    right_sum = subtreeSum(root.right)
    return root.data + left_sum + right_sum
    
def sumSubtree(root, sum): 
	cur_sum = [] 
	cur_sum.append(root)
	while cur_sum:
	  node=cur_sum.pop(0)
	  if node.left and node.right:
	    sum1=subtreeSum(node)
	    cur_sum.append(node.left)
	    cur_sum.append(node.right)
	  if sum1==sum:
	    return True
    

if __name__ == '__main__': 

	root = newnode(8) 
	root.left = newnode(5) 
	root.right = newnode(4) 
	root.left.left = newnode(9) 
	root.left.right = newnode(7) 
	root.left.right.left = newnode(1) 
	root.left.right.right = newnode(12) 
	root.left.right.right.right = newnode(2) 
	root.right.right = newnode(11) 
	root.right.right.left = newnode(3) 
	sum = 22

	if (sumSubtree(root, sum)) : 
		print("Yes" ) 
	else: 
		print("No") 
