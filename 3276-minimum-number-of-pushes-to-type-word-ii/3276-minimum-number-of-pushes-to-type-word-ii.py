class Solution:
    def minimumPushes(self, word: str) -> int:
        hm={}
        for i in word:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        ans=0
        counter=0
        for val in sorted(hm.values(), reverse=True):
            if counter<8:
                ans+=val
            elif(counter>=8 and counter<16):
                ans+=(val*2)
            elif(counter>=16 and counter<24):
                ans+=(val*3)
            else:
                ans+=(val*4)
            counter+=1
        return ans
            
        