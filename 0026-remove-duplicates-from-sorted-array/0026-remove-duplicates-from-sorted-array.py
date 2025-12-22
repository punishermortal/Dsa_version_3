class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        change = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[change]=nums[i]
                change+=1
        return change
        