from collections import deque
class stack:
  def __init__(self):
    self.q=deque()
    
  def push(self,data):
    s=len(self.q)
    self.q.append(data)
    for i in range(s):
      self.q.append(self.q.popleft())
    print(f"pushed {data} to the stack")
  def pop(self):
    if len(self.q)==0:
      return False
    return self.q.popleft()
      
  def printq(self):
    s=len(self.q)
    for i in range(s):
      print(self.q[i],end=" ")
    print()

  def top(self):
    if len(self.q)==0:
      return False
    return self.q[0]


st=stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print("stack elements:")
st.printq()
print(st.pop(),"popped from stack")
print(st.top(),"popped from stack")
