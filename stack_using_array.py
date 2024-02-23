def createstack():
  stack=[]
  return stack 

def isempty(stack):
  return len(stack)==0

def push(stack,data):
  stack.append(data)
  print(f"{data} is pushed into stack ")
  
def pop(stack):
  if isempty(stack):
    return False
  return stack.pop()
  
def peek(stack):
  if isempty(stack):
    return False
  return stack[len(stack)-1]
  
st=createstack()
push(st,1)
push(st,2)
push(st,3)
push(st,4)
print("stack ele:")
print(st)
pop(st)
print("stack ele after popping 1 ele:")
print(st)
print("top val:",peek(st))
print("isempty:",isempty(st))