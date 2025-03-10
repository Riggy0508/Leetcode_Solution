// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        l=0
        r=1

        while r<len(prices):
            if prices[r]>prices[l]:
                maxProfit=max(maxProfit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProfit
                
                