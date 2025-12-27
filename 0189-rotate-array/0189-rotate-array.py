# (i+k)%len(n)  --->>>> potion of every element


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse_array(nums ,0 , len(nums)-1)
        self.reverse_array(nums ,0 , k-1)
        self.reverse_array(nums ,k , len(nums)-1)
    def reverse_array(self , nums ,start ,end):
        while(start < end):
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        return nums
        