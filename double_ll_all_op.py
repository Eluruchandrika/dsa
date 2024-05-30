class node:
  def __init__(self,data):
    self.data=data
    self.next=None

class double_ll:
  def __init__(self):
    self.head=None
  
  def insert_at_beg(self,data):
    new_node=node(data)
    new_node.prev=None
    new_node.next=self.head
    if self.head:
      self.head.prev=new_node
    self.head = new_node
  def insert_after_val(self,val,new_data):
    new_node=node(new_data)
    curr=self.head
    while True:
      if curr.data==val:
        new_node.next=curr.next
        curr.next.prev=new_node
        curr.next=new_node
        new_node.prev=curr
        return
      else:
        curr=curr.next
  def insert_at_end(self,new_data):
    new_node=node(new_data)
    new_node.next=None
    curr=self.head
    while curr.next!=None:
      curr=curr.next
    curr.next=new_node
    new_node.prev=curr
      
  def del_at_beg(self):
    self.head=self.head.next
    self.head.prev=None
    
  def del_val(self,val):
    curr = self.head
    while curr:
      if curr.next.data==val:
        curr.next.next.prev=curr
        curr.next=curr.next.next
        return
      else:
        curr=curr.next
  def del_at_end(self):
    curr=self.head
    while curr.next.next!=None:
      curr=curr.next
    curr.next=None
  def length_ll(self):
    curr=self.head
    length=0 
    while curr:
      length+=1 
      curr=curr.next
    print(length)
  def reverse(self):
    temp = None
    current = self.head
    while current is not None:
      temp = current.prev
      current.prev = current.next
      current.next = temp
      current = current.prev
    if temp is not None:
      self.head = temp.prev  
    
  def print_ll(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
if __name__=='__main__':
  ll=double_ll()
  for i in range(10,0,-1):
    ll.insert_at_beg(i)
  ll.insert_after_val(6,29)
  ll.insert_at_end(57)
  ll.del_at_beg()
  ll.del_val(8)
  ll.del_at_end()
  ll.reverse()
  ll.print_ll()
  # ll.length_ll()
  