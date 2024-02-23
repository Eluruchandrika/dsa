def postfix_to_infix(exp):
  stack=[]
  for i in exp:
    if i.isalnum():
      stack.append(i)
    else:
      op1=stack.pop()
      op2=stack.pop()
      stack.append("("+op2+i+op1+")")
  return stack.pop()
  
postfix_exp='ab-c+'
print(postfix_to_infix(postfix_exp))