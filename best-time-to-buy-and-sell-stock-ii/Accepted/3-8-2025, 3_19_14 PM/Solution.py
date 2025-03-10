// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        for r in range(1,len(prices)):
            if prices[r]>prices[r-1]:
                profit+=(prices[r]-prices[r-1])

        return profit