// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero,one=s.count("0"),0
        output=zero

        for i in s:
            if i=="0":
                zero-=1
            if i=="1":
                one+=1
            
            output=min(output,one+zero)
        return output