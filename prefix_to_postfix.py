def prefix_to_postfix(exp):
  stack=[]
  for i in reversed(exp):
    if i.isalnum():
      stack.append(i)
    else:
      op1=stack.pop()
      op2=stack.pop()
      stack.append(op1+op2+i)
  return stack.pop()

exp='+-abc'
print(prefix_to_postfix(exp))
    