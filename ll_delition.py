class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class linkedlist:
  def __init__(self):
    self.head=None
    
  def insertatbeg(self,new_data):
    new_node=Node(new_data)
    new_node.next=self.head
    self.head=new_node
  def delatbeg(self):
    if self.head==None:
      print("empty ll")
    self.head=self.head.next
    
  def delatend(self):
    if self.head==None:
      print("empty ll")
    curr=self.head
    prev=None
    while curr.next!=None:
      prev=curr
      curr=curr.next
    prev.next=None
    
  def delval(self,val):
    curr=self.head
    prev=None
    if curr!=None and curr.data == val :
        self.head=curr.next
        curr=None
        return
    while curr:
      if curr.data==val:
        break
      prev=curr
      curr=curr.next
    if curr is None:
      return
    prev.next=curr.next
    curr=None
    
  def printll(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
    

ll=linkedlist()
ll.insertatbeg('5')
ll.insertatbeg('1')
ll.insertatbeg('25')
ll.insertatbeg('35')
ll.insertatbeg('45')
ll.insertatbeg('55')
ll.insertatbeg('65')
print("Linked list elements are:")
ll.printll()
ll.delatbeg()
print("Linked list after del at beg:")
ll.printll()
ll.delatend()
print("Linked list after del at end:")
ll.printll()
ll.delval('35')
print("Linked list after del specific val:")
ll.printll()