# first approach -> using array
# queue=[]
# queue.append('a')
# queue.append('b')
# queue.append('c')
# queue.append('d')
# print("queue:\n",queue)
# print(queue.pop(),"dequeued")
# print(queue.pop(),"dequeued")
# print("current queue:\n",queue)


# 2nd approach -> using deque from collections package
# from collections import deque 
# queue=deque()
# queue.append('a')
# queue.append('b')
# queue.append('c')
# queue.append('d')
# print("queue:\n",queue)
# print(queue.popleft(),"dequeued")
# print(queue.popleft(),"dequeued")
# print("current queue:\n",queue)


# 3rd approach -> using Queue from queue package
from queue import Queue
queue=Queue(maxsize=5)
queue.put('a')
queue.put('b')
queue.put('c')
queue.put('d')
print("Queue is full:",queue.full())
print("Queue elements :")
while queue.qsize()!=0:
  print(queue.get(),end=" ")

