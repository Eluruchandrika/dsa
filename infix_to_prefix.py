def infix_to_prefix(exp):
  stack=[]
  output=""
  precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
  for i in reversed(exp):
    if i ==')':
      stack.append(i)
    elif i.isalnum():
      output+=i
    elif i =='(':
      while stack and stack[-1]!=')':
        output+=stack.pop()
      stack.pop()
    else:
      while stack and stack[-1]!=')' and precedence[i]<precedence.get(stack[-1],0):
        output+=stack.pop()
      stack.append(i)
  while stack:
    output+=stack.pop()
  return output[::-1]
  
infix_exp='a+b-c'
print(infix_to_prefix(infix_exp))
      
    