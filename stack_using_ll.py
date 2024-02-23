class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class stack:
  def __init__(self):
    self.head=None
    
  def isempty(self):
    return self.head==None
    
  def push(self,data):
    newnode=node(data)
    newnode.next=self.head
    self.head=newnode
    print(f"{data} pushed to stack")
    
  
  def pop(self):
    if self.isempty():
      return False
    temp=self.head
    self.head=self.head.next
    return temp.data
  
  def peek(self):
    if self.isempty():
      return False
    return self.head.data 
    
  def printstack(self):
    curr=self.head
    while curr:
      print(curr.data,end=" ")
      curr=curr.next
    print()
    
  def minele(self):
    curr=self.head
    minval=self.head.data
    while curr:
      if curr.data<minval:
        minval=curr.data
      else:
        curr=curr.next
    return minval
    
    
    
    
if __name__=='__main__':
  st=stack()
  st.push(9)
  st.push(2)
  st.push(3)
  st.push(4)
  st.push(5)
  print("currunt stack is: ",end="")
  st.printstack()
  st.pop()
  print("stack after popping one ele is: ",end="")
  st.printstack()
  print("top ele of stack is: ",end="")
  print(st.peek())
  print("stack isempty: ",st.isempty())
  print("min val in stack is: ",st.minele()) 

  
    