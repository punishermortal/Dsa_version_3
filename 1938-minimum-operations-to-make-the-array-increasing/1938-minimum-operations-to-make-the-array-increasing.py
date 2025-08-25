class Solution:
    def minOperations(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            if nums[i]>curr:
                curr = nums[i]
            else:
                ans+= (curr - nums[i] + 1)
                curr = curr + 1
        return ans
        