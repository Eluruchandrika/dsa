class node:
  def __init__(self,data):
    self.data= data
    self.next=None
    
class linkedlist:
  def __init__(self):
    self.head=None
    
  def insert_at_beginning(self,new_data):
    new_node=node(new_data)
    new_node.next=self.head
    self.head=new_node 
    
  def insert_at_end(self,new_data):
    new_node=node(new_data)
    new_node.next=None
    if self.head is None:
      self.head=new_node
    else:
      curr=self.head
      while curr.next:
        curr=curr.next
      curr.next=new_node
      
  def insert_after_node(self,prev_node,new_data):
    if prev_node is None:
      print("node not existed in ll")
      return
    else:
      new_node=node(new_data)
      new_node.next=prev_node.next
      prev_node.next=new_node
      
  def del_at_beg(self):
    if self.head==None:
      return
    else:
      self.head=self.head.next
  def del_val(self,data):
    curr=self.head
    while curr.next:
      if curr.next.data==data:
        curr.next=curr.next.next
      curr=curr.next
  
  def del_at_end(self):
    if self.head==None or self.head.next==None:
      return None
    curr=self.head
    while curr.next.next:
      curr=curr.next
    curr.next=None
      
  def print_list(self):
    curr=self.head
    count=0
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
      count+=1
    print()
    
  def swap_nodes(self,x,y):
    x1=self.head
    y1=self.head
    while x1:
      if x1.data==x:
        break
      x1=x1.next
    while y1:
      if y1.data==y:
        break
      y1=y1.next
    x1.data,y1.data= y1.data,x1.data
    
  def reverse_ll(self):
    curr=self.head
    prev=None
    while curr:
      next,curr.next=curr.next,prev
      prev,curr=curr,next
    self.head=prev
    # or

    
  def len_ll(self):
    curr=self.head
    count=0
    while curr:
      curr=curr.next
      count+=1
    print(count)
    
  def find_nth_node(self,n):
    curr=self.head
    count=0
    while curr:
      if count==n:
        print(curr.data)
      curr=curr.next
      count+=1
      
  def findMidEle(self):
    slow=self.head
    fast=self.head
    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
    print("mid value is",slow.data)
  
  def count_num(self,num):
    curr=self.head
    count=0 
    while curr:
      if curr.data==num:
        count+=1
      curr=curr.next
    print(f"count of {num} is",count)
  
#alternative for reversing a ll 
def print_reverse(head):
    if not head:
        return
 
    print_reverse(head.next)
    print(head.data, end=" ")
    
    
def merge_two_sorted_lists(list1,list2):
    temp=None
    if list1 is None:
      return list2
    if list2 is None:
      return list1
    if list1.data<=list2.data:
      temp=list1
      temp.next=merge_two_sorted_lists(list1.next,list2)
    else:
      temp=list2
      temp.next=merge_two_sorted_lists(list1,list2.next)
    return temp  
    
if __name__=='__main__':
  ll1=linkedlist()
  ll2=linkedlist()
  ll3=linkedlist()
#   ll1.insert_at_beginning(1)
#   ll1.insert_at_beginning(4)
#   ll1.insert_at_beginning(5)
#   ll1.insert_at_beginning(7)
#   ll1.insert_at_beginning(9)
#   ll1.insert_at_beginning(10)
  for i in range(10,0,-1):
    ll1.insert_at_beginning(i)
  for i in range(10,5,-1):
    ll2.insert_at_beginning(i)
  # ll1.insert_at_end(15)
  # node1=ll1.head.next.next
  # ll1.insert_after_node(node1,29)
  #ll1.del_at_beg()
  #ll1.del_val(5)
  #ll1.del_at_end()
  # ll1.print_list()
  #ll1.swap_nodes(3,8)
  #ll1.reverse_ll()
  ll3.head=merge_two_sorted_lists(ll1.head,ll2.head)
  ll3.print_list()
  #ll1.findMidEle()
  #ll1.len_ll()
  #ll1.find_nth_node(3)
  #ll1.count_num(1)
  # print_reverse(ll1.head)
  # ll1.print_list()
