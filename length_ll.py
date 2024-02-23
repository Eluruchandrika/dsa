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
      
  def getlenofll(self):
    curr=self.head
    count=0
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
      count=count+1
    print()
    print("len of linkedlist:",count)
    
  # def getlen(self,node):
  #   if not node:
  #     return 0
  #   else:
  #     return 1 + self.getlenofll(self,node.next)
  # def getlenofll(self):
  #   return self.getlen(self.head)
    
    
    
if __name__=="__main__":
  ll=linkedlist()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)
  ll.insert(8)
  print("linked list elements:",end="")
  ll.getlenofll()
    
    