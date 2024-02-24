def next_greater_ele(arr):
  for i in range(len(arr)):
    next=-1
    for j in range(i+1,len(arr)):
      if arr[j]>arr[i]:
        next=arr[j]
        break
    print(arr[i],'->',next)  
    
arr=[1,4,7,2,9]
print("next greatest ele of each ele in array:")
next_greater_ele(arr)