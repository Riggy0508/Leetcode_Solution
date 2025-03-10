// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP=0
        profit=0

        l=r=0

        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            
            r+=1

        return maxP
            

                