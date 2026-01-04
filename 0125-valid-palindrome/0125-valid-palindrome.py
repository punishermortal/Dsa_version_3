class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for i in s:
            if (i>='a' and i<='z') or (i>='A' and i<='Z'):
                t+=i.lower()
            if (i>='0' and i<='9'):
                t+=str(i)
        print(t)
        return t.lower()==t[::-1].lower()
        