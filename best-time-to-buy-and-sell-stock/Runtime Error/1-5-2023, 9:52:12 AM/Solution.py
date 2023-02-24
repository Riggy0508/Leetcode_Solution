// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,len(prices)
        profit=0

        while r<len(prices):
            profit=max(profid,prices[])
