class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head = None 
    
  def insertatbeg(self,new_data):
    new_node=Node(new_data)
    new_node.next=self.head
    self.head=new_node
    
  def insertatend(self,new_data):
    new_node=Node(new_data)
    new_node.next=None
    curr=self.head
    while curr.next!=None:
      curr=curr.next
    curr.next=new_node
    
  def insertafter(self,new_data,node_data):
    new_node=Node(new_data)
    curr=self.head
    while curr:
      if curr.data==node_data:
        new_node.next=curr.next
        curr.next=new_node
      curr=curr.next

    
  def printlist(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    
      
if __name__=='__main__':
  LL=linkedlist()
  LL.insertatbeg(1)
  LL.insertatbeg(2)
  LL.insertatbeg(3)
  LL.insertatbeg(4)
  LL.insertatend(5)
  LL.insertafter(9,3)
  LL.printlist()
  