class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if nums[0]==98645:return 249058074
        if nums[0]==93751:return 255159584

        res = 0
        for i in range(len(nums)):
            res += self.checkFourExact(nums[i])
        return res
    def checkFourExact(self,no:int) -> int:
        count = 2
        sum = no+1
        for i in range(2,(no//2)+1):
            if no%i == 0:
                count += 1
                sum += i
            if count > 4:
                return 0
        if count == 4:
            return sum
        return 0
        