// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        r=l+1

        while r<len(prices):
            if prices[r]>prices[l]:
                profit=max(profit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return profit
