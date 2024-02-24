def sortstack(stack):
  temp_stack=[]
  while stack:
    temp=stack.pop()
    while temp_stack and temp_stack[-1]>temp:
      stack.append(temp_stack.pop())
    temp_stack.append(temp)
  return temp_stack
  
stack=[1,4,2,8]
print(sortstack(stack))
