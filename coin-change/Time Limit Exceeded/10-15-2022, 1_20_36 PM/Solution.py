// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans=self.coinChangeRecur(coins,0,amount)
        
        if ans==float("inf"):
            return -1
        else:
            return ans
        
    def coinChangeRecur(self,coins, index, amount):
        
        #base
        #valid
        if (amount==0):
            return 0
        
        #invalid
        if amount < 0 or index==len(coins):
            return math.inf
        
        #recurse
        #Select
        
        select=self.coinChangeRecur(coins,index,amount-coins[index])
        if select is not float("inf"):
            select+=1
        
        #notselect
        
        notSelect=self.coinChangeRecur(coins,index+1,amount)
        
        return min(select,notSelect)