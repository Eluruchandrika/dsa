class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def topView(self,root):
        if not root:
            return []
        left_nodes=[root]
        right_nodes=[root.right]
        result=[]
        while left_nodes:
            temp=left_nodes.pop(0)
            result.insert(0,temp.val)
            if temp.left:
                left_nodes.append(temp.left)
        while right_nodes:
            temp1=right_nodes.pop(0)
            result.append(temp1.val)
            if temp1.right:
                right_nodes.append(temp1.right)
        return result 
      
sol = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
print(sol.topView(root1)) 


