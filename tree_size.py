class Node:
     def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
def size(node):
    list1=[]
    list1.append(node)
    count=1
    while list1:
      temp=list1.pop(0)
      if temp.left:
        list1.append(temp.left)
        count+=1
      if temp.right:
        list1.append(temp.right)
        count+=1
    return count
# using recursion
def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+ 1 + size(node.right))     
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
 
print("Size of the tree is %d" %(size(root)))