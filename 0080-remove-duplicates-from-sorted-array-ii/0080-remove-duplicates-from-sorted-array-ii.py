class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:return len(nums)
        change = 2
        for i in range(2,len(nums)):
            if nums[change-2]!=nums[i]  :
                nums[change] =nums[i]
                change+=1
        return change

        