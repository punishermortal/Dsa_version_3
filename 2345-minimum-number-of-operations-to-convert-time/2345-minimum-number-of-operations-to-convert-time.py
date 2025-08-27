class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hr_cur,mn_cur = current.split(":")
        hr_sahi,mn_sahi = correct.split(":")
        # diff_hr=abs(int(hr_cur)-int(hr_sahi))
        # diff_min=abs(int(mn_cur)-int(mn_sahi))
        # print(diff_hr)
        # print(diff_min)
        # min_oper = (diff_min//60) + ((diff_min%60)//15) + ((diff_min%15)//5) + (diff_min%5)
        # return (diff_hr + min_oper)

        if int(hr_cur) < int(hr_sahi):
            diff_min = 60 - int(mn_cur) + (( int(hr_sahi) - (int(hr_cur) + 1)) * 60) + int(mn_sahi)
            print(mn_cur, (((int(hr_cur) + 1) - int(hr_sahi)) * 60))
        else:
            diff_min = int(mn_sahi) - int(mn_cur)
        print(hr_cur,hr_sahi)
        return  ((diff_min//60) + ((diff_min%60)//15) + ((diff_min%15)//5) + (diff_min%5))