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
  
    
  def remove_alternative_nodes(self):
    curr=self.head.next
    prev=self.head
    while curr:
      if prev.data==curr.data:
        prev.next=curr.next
      prev=curr
      curr=curr.next
    
    
    
if __name__=='__main__':
  ll1=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(2)
  ll1.insert(3)
  ll1.insert(3)
  ll1.insert(5)
  ll1.insert(6)
  print("ele of ll:")
  ll1.printll()
  ll1.remove_alternative_nodes()
  print("ele of ll after  removing alternative nodes:")
  ll1.printll()

  