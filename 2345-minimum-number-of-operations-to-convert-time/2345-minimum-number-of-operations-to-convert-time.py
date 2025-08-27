class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hr_cur,mn_cur = current.split(":")
        hr_sahi,mn_sahi = correct.split(":")

        if int(hr_cur) < int(hr_sahi):
            diff_min = 60 - int(mn_cur) + (( int(hr_sahi) - (int(hr_cur) + 1)) * 60) + int(mn_sahi)
        else:
            diff_min = int(mn_sahi) - int(mn_cur)
        return  ((diff_min//60) + ((diff_min%60)//15) + ((diff_min%15)//5) + (diff_min%5))