class Solution:
    def singleNumber(self, nums):
      list1=[]

      for i in range(len(nums)):
        if nums[i] not in list1:
          list1.append(nums[i])
        else:
          list1.remove(nums[i])
        
      return list1[0]
        
    
sol=Solution()
nums=[4,1,2,1,2]
print(sol.singleNumber(nums))
        