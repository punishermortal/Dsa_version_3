class Solution:
    def minTimeToType(self, word: str) -> int:
        initial='a'
        ans=0
        for char in word:
            rightside = abs(ord(char) - ord(initial))
            leftside = 26 - rightside
            ans+=min(leftside,rightside) +1
            initial = char
        return ans

