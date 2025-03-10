// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy=secondBuy=float('inf')
        firstProfit=0
        secondProfit=0


        for price in prices:
            firstBuy=min(firstBuy,price)
            firstProfit=max(firstProfit,price-firstBuy)
            secondBuy=min(secondBuy,price-firstProfit)
            secondProfit=max(secondProfit,price-secondBuy)

        return secondProfit
        