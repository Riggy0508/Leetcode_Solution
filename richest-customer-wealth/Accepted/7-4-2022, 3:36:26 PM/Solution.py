// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        
        for account in accounts:
            cur_wealth=sum(account)
            max_wealth=max(max_wealth,cur_wealth)
            
        return max_wealth