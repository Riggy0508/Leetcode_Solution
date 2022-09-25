// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        start=0
        result=[]
        prilen=len(prices)
        
        while (start<=prilen-1):
            curPrice=prices[start]
            next=start+1
            discount=-1
            while (next<=prilen-1):
                if prices[next]<=prices[start]:
                    discount=curPrice-prices[next]
                    break;
                next+=1
            if (discount>=0):
                result.append(discount)
            else:
                result.append(curPrice)
            start+=1
        return result