class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        change=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[change]=nums[i]
                change+=1
        # del nums[change:]
        return change

        