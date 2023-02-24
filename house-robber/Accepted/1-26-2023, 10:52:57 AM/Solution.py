// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        rob_neigh_next=0
        rob_neigh=nums[n-1]

        for i in range(n-2,-1,-1):
            cur=max(rob_neigh_next+nums[i],rob_neigh)
            rob_neigh_next=rob_neigh
            rob_neigh=cur
        return rob_neigh