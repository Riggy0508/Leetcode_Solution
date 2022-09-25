// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        
        while n:
            bit=n&1
            if bit==1:
                res+=1
            n=n>>1
        return res