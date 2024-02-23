class Node:
  def __init__(self,data):
    self.prev=None
    self.data=data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head=None
  def insertatbeg(self,data):
    newnode=Node(data)
    newnode.prev=None
    newnode.next=self.head
    self.head=newnode
    
  def insertatend(self,data):
    newnode=Node(data)
    newnode.next=None
    curr=self.head
    while curr.next!=None:
      curr=curr.next
    curr.next=newnode
    newnode.prev=curr
    
  def insertafter(self,data,node_data):
    newnode=Node(data)
    curr=self.head
    while curr:
      if curr.data==node_data:
        newnode.next=curr.next
        curr.next.prev=newnode
        curr.next=newnode
        newnode.prev=curr
        # break
      curr=curr.next
      
  def printll(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
    
    
if __name__=='__main__':
  ll=linkedlist()
  ll.insertatbeg(1)
  ll.insertatbeg(2)
  ll.insertatbeg(3)
  ll.insertatbeg(4)
  print("elements of ll after inserting the ele's at beginning: ",end="")
  ll.printll()  
  ll.insertatend(5)
  print("elements of ll after inserting one ele at end: ",end="")
  ll.printll()
  ll.insertafter(8,3)
  print("elements of ll after inserting ele 8 after 3: ",end="")
  ll.printll()