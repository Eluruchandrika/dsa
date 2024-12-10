class Solution:
  def findMaxConsecutiveOnes(self, nums):
    count=0
    maxVal=0
    for i in range(len(nums)):
      if nums[i] == 1:
        count=count+1
        if maxVal<count:
          maxVal=count
      else:
        count=0
    return maxVal
   
sol=Solution()
nums=[1,0,1,1,0,1]
print(sol.findMaxConsecutiveOnes(nums))
        