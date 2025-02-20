// https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1,n):
            if n%i==0:
                k-=1
                if k==0:
                    return i
            
        return n if k==1 else -1