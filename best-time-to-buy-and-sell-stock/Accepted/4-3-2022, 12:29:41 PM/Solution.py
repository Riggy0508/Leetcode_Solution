// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float('inf')
        max=0;
        
        for i in range(len(prices)):
            #print(prices[i])
            if prices[i]<min:
                min=prices[i]
            elif prices[i]-min>max:
                max=prices[i]-min
        return max
        