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
      newnode.next=self.head
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.next=newnode
      newnode.next=self.head
      self.head=newnode
      
      
  def delatbeg(self):
    if self.head==None:
      print("underflow")
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.next=self.head.next
      self.head=self.head.next
      
  def delatend(self):
    if self.head==None:
      print("underflow")
    else:
      curr=self.head
      prev=None
      while curr.next!=self.head:
        prev=curr
        curr=curr.next
      prev.next=self.head
      
  def delval(self,val):
    curr=self.head
    if self.head.data==val:
      self.delatbeg()
    else:
      while curr.next:
        if curr.next.data==val:
          curr.next=curr.next.next
          return
      curr=curr.next
        
        
        
    
      
  def printll(self):
    if self.head==None:
      print("list is empty")
    else:
      curr=self.head
      while curr:
          print(curr.data,end=' ')
          curr=curr.next
          if curr==self.head:
            break
      print()

if __name__=='__main__':
  ll=linkedlist()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)
  ll.insert(4)
  ll.insert(5)
  ll.insert(6)
  ll.insert(7)

  print("ele of linked list:")
  ll.printll()
  ll.delatbeg()
  print("ele of linked list after del at beg:")
  ll.printll()
  ll.delatend()
  print("ele of linked list after del at end:")
  ll.printll()
  ll.delval(4)
  print("ele of linked list after del specific ele(4):")
  ll.printll()
    