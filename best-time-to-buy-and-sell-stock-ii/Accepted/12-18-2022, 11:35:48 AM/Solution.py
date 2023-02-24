// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1

        output=0

        while r<len(prices):
            while r<len(prices)-1 and prices[l]>=prices[r]:
                l+=1
                r+=1
            while r<len(prices)-1 and prices[r+1]>prices[r]:
                r+=1
            if prices[r]>prices[l]:
                output+=(prices[r]-prices[l])

            l=r
            r+=1
        return output   
