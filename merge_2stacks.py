def create_stack():
    stack=[]
    return stack
    
def push(stack,data):
    stack.append(data)
    
def pop(stack):
    if not isempty():
      return False
    else:
      return stack.pop()
      
def peek(stack):
    if not isempty():
      return False
    else:
      return stack[-1]
  
def isempty(stack):
    return len(stack)==0

def merge_stacks(stack1,stack2):
    if len(stack1)==0 and len(stack2)==0:
        return
    else:
        for i in range(len(stack2)):
          stack1.append(stack2.pop())
    

st1=create_stack()
st2=create_stack()
push(st1,1)
push(st1,2)
push(st1,3)
push(st1,4)
push(st2,5)
push(st2,6)
push(st2,7)
push(st2,8)
print("stack1 ele:")
print(st1)
print("stack2 ele:")
print(st2)
merge_stacks(st1,st2)
print("elements after merging 2 stacks:")
print(st1)


