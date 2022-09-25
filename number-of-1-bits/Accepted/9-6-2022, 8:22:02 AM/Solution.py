// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        
        while n:
            bit=n&1
            if bit==1:
                ans+=1
            n=n>>1
        return ans