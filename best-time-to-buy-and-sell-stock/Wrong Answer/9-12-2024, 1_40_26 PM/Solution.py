// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l,r=0,1
        while r<len(prices):
            if prices[r]>prices[l]:
                profit=max(profit,prices[r]-prices[l])
            else:
                l+=1
            r+=1
        return profit