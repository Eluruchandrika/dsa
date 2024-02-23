def insert_botton_of_stack(stack,item):
  if len(stack)==0:
    stack.append(item)
  else:
    temp=stack.pop()
    insert_botton_of_stack(stack,item)
    stack.append(temp)

def reverse_stack(stack):
  if len(stack)>0:
    temp=stack.pop()
    reverse_stack(stack)
    insert_botton_of_stack(stack,temp)
    
# def reverse_stack(stack):
#   size=len(stack)
#   for i in range(size//2):
#     stack[i],stack[size-1-i]=stack[size-1-i],stack[i]
    

stack=[1,2,3,4,5]
reverse_stack(stack)
print(stack)
    
    