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
  
    
  def mov_mid_ele_to_first(self):
    try:
      fast=self.head
      slow=self.head
      prev=None
      while fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
      prev.next=slow.next
      slow.next=self.head
      self.head=slow
      # slow.data,self.head.data=self.head.data,slow.data
    except AttributeError:
      print("no mid ele")
    
    
if __name__=='__main__':
  ll1=linkedlist()
  ll1.insert(1)
  ll1.insert(2)
  ll1.insert(3)
  ll1.insert(4)
  ll1.insert(5)
#   ll1.insert(6)
  print("ele of ll:")
  ll1.printll()
  ll1.mov_mid_ele_to_first()
  print("ele of  ll after moving mid ele to first:")
  ll1.printll()
  

  