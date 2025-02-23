// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0


        for r in range(len(prices)):
            if prices[r]>prices[l]:
                profit=max(profit,prices[r]-prices[l])
            else:
                l=r

            r+=1

        return profit
            