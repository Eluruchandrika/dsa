class Solution:
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]

sol=Solution()
nums=[1,2,3,3]
print(sol.majorityElement(nums))