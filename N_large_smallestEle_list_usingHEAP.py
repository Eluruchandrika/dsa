import heapq
li=[2,5,3,9,1,6]
heapq.heapify(li)
print("Top 2 largest elements:",heapq.nlargest(2,li)) #print top 2 largest elements from list
print("Least 2 smallest elements:",heapq.nsmallest(2,li)) #print last 2 smallest elements from list
