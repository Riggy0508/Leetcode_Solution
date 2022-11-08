// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        len1=len(nums)
        
        if len1==1:
            return nums[0]
        
        rob_neighbour_next=0
        rob_neighbour=nums[len1-1]
        
        for i in reversed(range(nums[len1-2])):
            cur=max(rob_neighbour_next+nums[i],rob_neighbour)
            
            rob_neighbour_next=rob_neighbour
            rob_neighbour=cur
            
        return rob_neighbour
            
        
        
#         n=len(nums)
        
#         if n==1:
#             return nums[0]
        
#         rob_next_next=0
#         rob_next=nums[n-1]
        
#         for i in range(n-2,-1,-1):
#             cur=max(nums[i]+rob_next_next,rob_next)
            
#             rob_next_next=rob_next
#             rob_next=cur
#         return rob_next