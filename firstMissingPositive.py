class Solution:
    def firstMissingPositive(self, nums):
      nums=set(nums)
      for i in range(1,len(nums)+1):
        if i not in nums:
          return i
      return len(nums)+1        

sol=Solution()
nums=[1,2,0]
print(sol.firstMissingPositive(nums))
