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
    
  def isidentical(self,listb):
    a=self.head
    b=listb.head
    while a and b:
      if a.data==b.data:
        a=a.next
        b=b.next
        return True
      return False
    # return a==None and b==None
      
    
if __name__=='__main__':
  ll1=linkedlist()
  ll2=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(3)
  ll2.insert(1)
  ll2.insert(2)
  ll2.insert(3)
  print(ll1.isidentical(ll2))

  