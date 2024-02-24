import heapq
li1=[9,4,2,7]
li2=[18,5,327,8]
heapq.heapify(li1)
heapq.heapify(li2)
print("initial list1:")
print(list(li1))
print("initial list2:")
print(list(li2))
heapq.heappush(li1,5)#push 5 to li1
heapq.heappush(li2,1)#push 1 to li2
print("lists after pushing ele's in list1 and list2:")
print(list(li1))
print(list(li2))
heapq.heappop(li1) #remove small ele
heapq.heappop(li2) #remove small ele
print("lists after popping ele's in list1 and list2:")
print(list(li1))
print(list(li2))
print("popped ele:",heapq.heappushpop(li1,10))#push 10 pop smallest ele
print("list1 after performing heappushpop op:")
print(list(li1))
print("popped ele:",heapq.heapreplace(li2,13))#push 13 pop smallest ele
print("list1 after performing heapreplace op:")
print(list(li2))

