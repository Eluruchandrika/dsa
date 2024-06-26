def parentheses(string):
    stack=[]
    count=0
    for i in string:
        if i.isalnum() or i=='{' or i=='[' or i=='(':
            stack.append(i)
        if i=='}':
            while stack:
              x=stack.pop()
              if x=='{':
                  count+=1
                  break
              if x=='(' or x=='[':
                  return 0 
        if i==']':
            while stack:
              x=stack.pop()
              if x=='[':
                  count+=1
                  break
              if x=='(' or x=='{':
                  return 0  
        if i==')':
            while stack:
              x=stack.pop()
              if x=='(':
                  count+=1
                  break
              if x=='[' or x=='{':
                  return 0
    return count 