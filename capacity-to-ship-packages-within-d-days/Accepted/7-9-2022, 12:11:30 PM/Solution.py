// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        
        while l<r:
            mid=(l+r)//2
            
            if self.can_ship(mid,weights,days):
                r=mid
            else:
                l=mid+1
                
        return r
    
    
    def can_ship(self,candidate,weights,days):
        cur_weight=0
        days_taken=1
        
        for weights in weights:
            cur_weight+=weights
            
            if cur_weight>candidate:
                days_taken+=1
                cur_weight=weights
                
        return days_taken<=days
        