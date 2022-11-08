// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        rob_next_next=0
        rob_next=nums[n-1]
        
        for i in range(n-2,-1,-1):
            
            cur=max(rob_next_next+nums[i],rob_next)
            
            rob_next_next=rob_next
            rob_next=cur
        return rob_next
            
        