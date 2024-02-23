class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head=None
    
  def insertatbeg(self,data):
    newnode=node(data)
    if self.head == None:
      self.head=newnode
      newnode.next=self.head
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.next=newnode
      newnode.next=self.head
      self.head= newnode
      
  def insertatend(self,data):
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
      
  def insertafterval(self,data,node_val):
    newnode=node(data)
    curr=self.head
    while curr:
      if curr.data==node_val:
        newnode.next=curr.next
        curr.next=newnode
        return
      curr=curr.next
    

  def printll(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
      if curr==self.head:
        break
    print()
      
if __name__=='__main__':
  ll=linkedlist()
  ll.insertatbeg(1)
  ll.insertatbeg(2)
  ll.insertatbeg(3)
  ll.insertatbeg(4)
  print("ele of ll after insering at beg:")
  ll.printll()
  ll.insertatend(5)
  print("ele of ll after insering one ele at end:")
  ll.printll()
  ll.insertafterval(9,3)
  print("ele of ll after insering 9 after 3 :")
  ll.printll()