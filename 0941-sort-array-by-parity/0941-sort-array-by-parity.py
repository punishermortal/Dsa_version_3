class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        n = len(nums)
        end = n-1
        while(start < end):
            if nums[end] % 2 == 0 and nums[start] % 2 != 0:
                nums[end],nums[start] = nums[start],nums[end]
                end -= 1
                start += 1
            elif nums[start] % 2 == 0 and nums[end] % 2 == 0:
                start += 1
            else:
                end -= 1
        return nums



        