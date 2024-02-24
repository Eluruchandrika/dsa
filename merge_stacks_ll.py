class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class stack:
  def __init__(self):
    self.head=None
    
  def isempty(self):
    return self.head is None

  def push(self,data):
    newnode=node(data)
    if self.isempty():
      self.head=newnode
    else:
      newnode.next=self.head
      self.head=newnode
  
  def top(self):
    if self.isempty():
      print("underflow")
    else:
      return self.head.data
      
  def pop(self):
    if self.isempty():
      print("underflow")
    else:
      print(self.head.data,"is popped \ncurrent stack:")
      self.head=self.head.next
      
  def merge_stacks(self,stack2):
      if self.head is None and stack2.head is None:
        return
      else:
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=stack2.head
        
  def print_stack(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
    

st1=stack()
st1.push(1)
st1.push(2)
st1.push(3)
st1.push(4)
# print(st.isempty())
print("stack1 ele:")
st1.print_stack()
st1.pop()
st1.print_stack()
print("top ele of stack1:", st1.top())
st2=stack()
st2.push(5)
st2.push(6)
st2.push(7)
st2.push(8)
print("stack2 ele:")
st2.print_stack()
st1.merge_stacks(st2)
print("stack1 after merging stack2")
st1.print_stack()

  