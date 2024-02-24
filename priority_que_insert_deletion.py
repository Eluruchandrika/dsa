class pqueue:
  def __init__(self):
    self.queue=[]
    
  def insert(self,data,priority):
      self.queue.append((data,priority))
      
  def isempty(self):
    return len(self.queue)==0
      
  def delete(self):
    for i in range(len(self.queue)):
      maxpriorty=self.queue[0][1]
      index_1=0
      if self.queue[i][1]>maxpriorty:
        maxpriorty=self.queue[i][1]
        index_1=i
        
    return self.queue.pop(index_1)
    
      
if __name__=='__main__':
  pq=pqueue()
  pq.insert(5,9)
  pq.insert(15,3)
  pq.insert(35,5)
  print("deleteing elements which having highest priority:")
  while not pq.isempty():
    print(pq.delete())
  
  