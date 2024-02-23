def balenced_parameters(exp):
  stack=[]
  for i in exp:
    if  i in ['{','[','(']:
      stack.append(i)
    else:
      if not stack:
        return False
      curr_top=stack.pop()
      if i=='}':
        if curr_top !='{':
          return False
      
      elif i==']':
        if curr_top !='[':
          return False
      
      elif i==')':
        if curr_top !='(':
          return False
  
  if stack:
    return False
  return True
        
exp='({})[]'
print(balenced_parameters(exp))