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
    
  def findmidele(self):
    slow=self.head
    fast=self.head
    while fast.next:
      slow=slow.next
      fast=fast.next.next
    print(slow.data)
      
    
if __name__=='__main__':
  ll1=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(3)
  ll1.insert(4)
  ll1.insert(5)
  # ll1.insert(6)
  print("linked list ele's:")
  ll1.printll()
  print("mid ele of linked list:")
  ll1.findmidele()

  