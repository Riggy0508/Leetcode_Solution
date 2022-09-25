// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        
        maxP=0
        
        while r<len(prices):
            if prices[l]< prices[r]:
                maxP=max(maxP,prices[r]-prices[l])
            else:
                l+=1
            r+=1
            
        return maxP