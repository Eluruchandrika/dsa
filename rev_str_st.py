def rev_str(string):
  stack=[]
  for i in string:
    stack.append(i)
  while stack:
    print(stack.pop(),end="")
    
string='hi me'
rev_str(string)