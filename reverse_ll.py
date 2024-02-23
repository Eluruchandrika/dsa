class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head=None
  def insert(self,data):
    newnode=node(data)
    if self.head==None:
      self.head=newnode
    else:
      newnode.next=self.head
      self.head=newnode
      
  def printll(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
    
  def revll(self):
    curr=self.head
    prev=None
    while curr:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.head=prev
    
    
if __name__=='__main__':
  ll=linkedlist()
  ll.insert(4)
  ll.insert(3)
  ll.insert(2)
  ll.insert(1)
  print("ele of linkedlist :")
  ll.printll()
  ll.revll()
  print("ele of ll after reversing : ")
  ll.printll()
  