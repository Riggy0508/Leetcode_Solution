// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=0,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
                
            if hours<=h:
                res=min(res,k)
                r-=1
            else:
                l+=1
        return res