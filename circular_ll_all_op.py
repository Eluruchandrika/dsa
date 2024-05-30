class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class circular_ll:
  def __init__(self):
    self.head=None
  def insert_at_beg(self,new_data):
    new_node=node(new_data)
    if self.head==None:
      self.head=new_node
      new_node.next=self.head
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.next=new_node
      new_node.next=self.head
      self.head=new_node
  def insert_after_node(self,key,new_data):
    new_node=node(new_data)
    curr=self.head
    while True:
      if curr.data==key:
        new_node.next=curr.next
        curr.next=new_node
        break
      curr=curr.next
  def insert_at_end(self,new_data):
    new_node=node(new_data)
    if self.head==None:
      self.head=new_node
      new_node.next=self.head
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.next=new_node
      new_node.next=self.head
  def del_at_beg(self):
    if self.head==None or self.head.next==self.head:
      return None
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.next=self.head.next
      self.head=self.head.next
      
  def del_val(self,val):
    if self.head.data==val:
      self.head=self.head.next
      return
    else:
      curr=self.head
      while curr:
        if curr.next.data==val:
          curr.next=curr.next.next
          return
        else:
          curr=curr.next
  def del_at_end(self):
    if self.head==None or self.head.next==self.head:
      return None
    else:
      curr=self.head
      while curr.next.next!=self.head:
        curr=curr.next
      curr.next=self.head
  
  def is_circular(self): 
    if self.head is None: 
      return False
    slow = self.head 
    fast = self.head.next
    while fast is not None and fast.next is not None: 
      if slow == fast: 
        return True
      slow = slow.next
      fast = fast.next.next
    return False
    
  def length_ll(self):
    curr=self.head
    count=1
    while curr.next!=self.head:
      count+=1
      curr=curr.next
    return count
    
  def print_ll(self):
    curr=self.head
    while True:
      print(curr.data, end=" ")
      curr=curr.next
      if curr==self.head:
        break
  def swap_first_last_nodes(self):
    if self.head==None:
      print("empty ll")
    else:
      curr=self.head
      while curr.next!=self.head:
        curr=curr.next
      curr.data,curr.next.data=curr.next.data,curr.data
  
  def slipt_into_twohalfs(self):
    if self.head==None:
      print("empty ll")
    else:
      curr=self.head
      length=self.length_ll()
      half=length//2
      count=1
      print("first half:")
      while curr:
        print(curr.data,end=" ")
        if count==half:
          break
        curr=curr.next
        count+=1
      print()
      curr=self.head
      count=1
      print("second half: ")
      while curr.next!=self.head:
        if count>=half:
          print(curr.next.data,end=" ")
          count+=1
          curr=curr.next
        else:
          count+=1
          curr=curr.next
      print()
      
  def insert_into_sortedLL(self,new_data):
    if self.head==None:
      print("empty ll")
    else:
      new_node=node(new_data)
      curr=self.head
      while curr.next!=self.head:
        if curr.data < new_data and curr.next.data > new_data:
          new_node.next=curr.next
          curr.next=new_node
          return
        else:
          curr=curr.next
if __name__=='__main__':
  ll=circular_ll()
  # for i in range(11,0,-1):
  #   ll.insert_at_beg(i)
  # ll.insert_after_node(1,20)
  # ll.insert_at_end(90)
  # # ll.del_at_beg()
  # ll.del_val(4)
  # ll.del_at_end()
  # print(ll.is_circular())
  # ll.length_ll()
  # ll.swap_first_last_nodes()
  # ll.slipt_into_twohalfs()
  ll.insert_at_beg(15)
  ll.insert_at_beg(11)
  ll.insert_at_beg(9)
  ll.insert_at_beg(5)
  ll.insert_at_beg(3)
  ll.insert_at_beg(1)
  ll.insert_into_sortedLL(14)
  ll.print_ll()
  
    