class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        for k,v in hm.items():
            if v >= n/2:
                return k
        return 0
        