class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
      if root is None:
        return
      result=[]
      list1=[root]
      while list1:
        length =len(list1)
        list2=[]
        while length>0:
          temp=list1.pop(0)
          list2.append(temp.val)
          if temp.left:
            list1.append(temp.left)
          if temp.right:
            list1.append(temp.right)
          length-=1
        result.append(list2)
      return result
      
sol = Solution()
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(sol.levelOrder(root1)) 


