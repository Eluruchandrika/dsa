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
    
  def sum_of_last_Nnodes(self,n):
    curr=self.head
    length=0
    while curr:
      length=length+1
      curr=curr.next
    position=length-n
    curr=self.head
    count=0
    sum=0
    while curr:
      if count>=position:
        sum+=curr.data
        count=count+1
      count=count+1 
      curr=curr.next
    print(sum)
    
    
if __name__=='__main__':
  ll1=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(4)
  ll1.insert(3)
  ll1.insert(5)
  ll1.insert(6)
  ll1.insert(9)
  print("ele in linked list:")
  ll1.printll()
  print("sum of last 5  nodes in linked list:")
  ll1.sum_of_last_Nnodes(5)
