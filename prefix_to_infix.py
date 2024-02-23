def prefix_to_infix(exp):
  stack=[]
  for i in reversed(exp):
    if i.isalnum():
      stack.append(i)
    else:
      op1=stack.pop()
      op2=stack.pop()
      stack.append("("+op1+i+op2+")")
  return stack.pop()
  
prefix_exp='+-abc'
print(prefix_to_infix(prefix_exp))