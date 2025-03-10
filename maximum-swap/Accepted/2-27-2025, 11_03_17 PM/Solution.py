// https://leetcode.com/problems/maximum-swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        maxi=0
        maxD="0"

        num=list(str(num))

        a,b=0,0

        for i in range(len(num)-1,-1,-1):
            if num[i]>maxD:
                maxD=num[i]
                maxi=i

            if num[i]<maxD:
                a,b=i,maxi

        num[a],num[b]=num[b],num[a]

        return int("".join(num))