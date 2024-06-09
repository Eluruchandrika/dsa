class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def LeftView(root):
    list1=[root]
    result=[]
    while list1:
        temp=list1.pop(0)
        result.append(temp.val)
        if temp.left:
            list1.append(temp.left)
        elif temp.right:
            list1.append(temp.right)
        else:
            return result
      
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.left.left.right=TreeNode(8)
print("left view:")
print(*LeftView(root1)) 


