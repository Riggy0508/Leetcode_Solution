// https://leetcode.com/problems/coin-change

class Solution:
    
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for x in range(amount+1)]for x in range(len(coins)+1)]
        
        ans=self.coinChangeRecur(coins,0,amount,dp)
        if ans==math.inf:
            return -1
        else:
            return ans
        
    def coinChangeRecur(self,coins, index, amount,dp):
        
        #base
        #valid
        if (amount==0):
            return 0
        
        #invalid
        if amount < 0 or index==len(coins):
            return math.inf
        
        #recurse
        #Select
        
        if dp[index][amount]==0:
            
            select=self.coinChangeRecur(coins,index,amount-coins[index],dp)
            if select is not math.inf:
                select+=1

            #notselect

            notSelect=self.coinChangeRecur(coins,index+1,amount,dp)
            
            dp[index][amount]=min(select,notSelect)
        
        return dp[index][amount]