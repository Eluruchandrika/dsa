from queue import Queue
# def rev_queue_using_st(queue):
#     stack=[]
#     while not queue.empty():
#         stack.append(queue.get())
#     while stack:
#         queue.put(stack.pop())
#     return queue

def rev_queue_using_st(queue):
    if queue.empty():
      return
    temp=queue.get()
    rev_queue_using_st(queue)
    queue.put(temp)
q=Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
rev_queue_using_st(q)
print("reversed queue:")
while not q.empty():
    print(q.get(),end=" ")
