// https://leetcode.com/problems/maximum-swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        max_i=-1
        max_digit="0"
        swapI,swapJ=-1,-1

        for i in range(len(num)-1,-1,-1):
            if num[i]>max_digit:
                max_digit=num[i]
                max_i=i
            
            if num[i]<max_digit:
                swapI,swapJ=i,max_i
            #print(max_digit,max_i,"|",i)

        num[swapI],num[swapJ]=num[swapJ],num[swapI]

        return int("".join(num))

