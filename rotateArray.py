class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

sol=Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(nums,k))
