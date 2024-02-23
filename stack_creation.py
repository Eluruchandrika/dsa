# stack=[]
# from collections import deque
# stack=deque()
# stack.append('a')
# stack.append('b')
# stack.append('c')
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


from queue import LifoQueue
stack=LifoQueue(maxsize=3)
stack.put('a')
stack.put('b')
stack.put('c')
# print(stack)
print("size:",stack.qsize())
print("isfull:",stack.full())
print(stack.get(),"popped from stack")
print(stack.get(),"popped from stack")
print(stack.get(),"popped from stack")
print("isempty:",stack.empty())

