class Node:
  def __init__(self,data):
    self.prev=None
    self.data=data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head=None
    
  def insert(self,data):
    newnode=Node(data)
    newnode.prev=None
    if self.head is None:
      self.head=newnode
    else:
      newnode.next=self.head
      self.head.prev=newnode
      self.head=newnode
      
  def delatbeg(self):
    self.head=self.head.next
    self.head.prev=None
    
  def delatend(self):
    curr=self.head
    prev=None
    while curr.next!=None:
      prev=curr
      curr=curr.next
    curr.prev=None
    prev.next=None
    
  def delval(self,val):
    curr=self.head
    prev=None
    if self.head.data==val:
      self.head=self.head.next
      return
    # prev=None
    while curr:
      if curr.data==val:
        prev.next=curr.next
        curr.next.prev=prev
        return
      else:
        prev=curr
        curr=curr.next
      if curr.data==val and curr.next==None:
        prev.next=None
        return
      
        
    
    
  def printll(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
    
    
    
if __name__=='__main__':
  ll=linkedlist()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)
  ll.insert(4)
  ll.insert(5)
  ll.insert(6)
  print("ele in linkedlist are:")
  ll.printll()
  ll.delatbeg()
  print("ele in linkedlist after del at beg are:")
  ll.printll()
  ll.delatend()
  print("ele in linkedlist after del at end are:")
  ll.printll()
  ll.delval(4)
  print("ele in linkedlist after del node 4 are:")
  ll.printll()