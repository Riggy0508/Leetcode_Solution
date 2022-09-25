// https://leetcode.com/problems/maximum-number-of-accepted-invitations

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        boys=len(grid)
        girls=len(grid[0])
        ans=0
        partner=[-1]*girls
        
        def canInvite(i,seen):
            for j in range(girls):
                if not grid[i][j] or seen[j]:
                    continue
                seen[j]=True
                if partner[j]==-1 or canInvite(partner[j],seen):
                    partner[j]=i
                    return True
            return False
        
        for i in range(boys):
            seen=[False]*girls
            if canInvite(i,seen):
                ans+=1
                
        return ans