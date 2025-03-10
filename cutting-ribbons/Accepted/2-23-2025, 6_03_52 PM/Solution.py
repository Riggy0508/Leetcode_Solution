// https://leetcode.com/problems/cutting-ribbons

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        low=1
        high=max(ribbons)

        while low <=high:
            mid=(low+high)//2
            totalCNT=sum(ribbon//mid for ribbon in ribbons)
            if totalCNT>=k:
                low=mid+1
            else:
                high=mid-1
        return low-1