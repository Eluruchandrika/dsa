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
  
  def swaplastfirstele(self):
    curr=self.head
    prev=None
    while curr.next!=None:
      prev=curr
      curr=curr.next
    curr.next=self.head.next
    prev.next=self.head
    self.head.next=None
    self.head=curr
    
if __name__=='__main__':
  ll1=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(3)
  ll1.insert(4)
  ll1.insert(5)
  ll1.insert(6)
  print("ele of ll:")
  ll1.printll()
  ll1.swaplastfirstele()
  print("ele of ll  after swapping last and first ele:")
  ll1.printll()

  