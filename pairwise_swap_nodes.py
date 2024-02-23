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
    
  def pairwise_swap_nodes(self):
    if self.head==None:
      return
    curr=self.head
    while curr:
      curr.data,curr.next.data=curr.next.data,curr.data
      curr=curr.next.next
      
      
    
    
if __name__=='__main__':
  ll1=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(4)
  ll1.insert(3)
  ll1.insert(5)
  ll1.insert(6)
  print("ele of ll:")
  ll1.printll()
  ll1.pairwise_swap_nodes()
  print("ele of linked list  after swapping pairs:")
  ll1.printll()