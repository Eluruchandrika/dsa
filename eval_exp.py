def infix_to_postfix(exp):
  stack=[]
  output=""
  precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
  for i in exp:
    if i=='(':
      stack.append(i)
    elif i.isdigit():
      output+=i
    elif i==')':
      while stack and stack[-1]!='(':
        output+=stack.pop()
      stack.pop()
    else:
      while stack and precedence[i]<precedence.get(stack[-1],0):
        output+=stack.pop()
      stack.append(i)
  while stack:
    output+=stack.pop()
  return output 
  
def eval_exp(exp):
  stack=[]
  for i in exp:
    if i.isdigit():
      stack.append(int(i))
    else:
      op1=stack.pop()
      op2=stack.pop()
      if i=='+':
        result= op1+op2
      elif i=='-':
        result= op1-op2
      elif i=='*':
        result= op1*op2
      elif i=='/':
        result= op1/op2
      stack.append(result)
    #   stack.append(str(eval(op2+i+op1)))

  return stack.pop()
  
exp='(1+2)+1'
x=infix_to_postfix(exp)
print(eval_exp(x))