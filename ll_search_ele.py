class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head=None
    
  def insetnode(self,data):
    newnode=Node(data)
    newnode.next=self.head
    self.head=newnode
    
  def searchele(self,ele):
    curr=self.head
    while curr:
      if curr.data==ele:
        return True
      curr=curr.next
    return False
  
if __name__=='__main__':
  ll=linkedlist()
  ll.insetnode(1)
  ll.insetnode(2)
  ll.insetnode(3)
  ll.insetnode(4)
  print("search ele not in list",ll.searchele(5))
  print("search ele which is in list",ll.searchele(5))