class queue:
  def __init__(self):
    self.s1=[]
    self.s2=[]
  def enqueue(self,x):
    self.s1.append(x)
    print(f"{x} is ennqueued into queue")
  def dequeue(self):
    if len(self.s1)==0 and len(self.s2)==0:
      return False
    elif len(self.s1)>0 and len(self.s2)==0:
      while len(self.s1):
        self.s2.append(self.s1.pop())
      return self.s2.pop()
    elif len(self.s1)==0 and len(self.s2)>0:
      return self.s2.pop()
    elif len(self.s1)>0 and len(self.s2)>0:
      return self.s2.pop()
      
  def printque(self):
    if len(self.s1)==0 and len(self.s2)==0:
      return False
    if len(self.s1)>0 and len(self.s2)==0:
      for i in range(len(self.s1)):
        print(self.s1[i],end=" ")
      print()
      
    elif len(self.s1)==0 and len(self.s2)>0:
      for i in range(len(self.s2)-1,-1,-1):
        print(self.s2[i],end=" ")
      print()
    elif len(self.s1)>0 and len(self.s2)>0:
      for i in range(len(self.s2)-1,-1,-1):
        print(self.s2[i],end=" ")
      for i in range(len(self.s1)):
        print(self.s1[i],end=" ")
      
      
if __name__=='__main__':
  que=queue()
  que.enqueue(1)
  que.enqueue(2)
  que.enqueue(3)
  que.enqueue(4)
  que.enqueue(5)
  print("queue ele:")
  que.printque()
  print(que.dequeue(),"is dequeued from queue")
  print(que.dequeue(),"is dequeued from queue")
  print(que.dequeue(),"is dequeued from queue")
  print("current queue ele:")
  que.printque()
  que.enqueue(6)
  que.enqueue(8)
  print("current queue ele:")
  que.printque()
  

  
  