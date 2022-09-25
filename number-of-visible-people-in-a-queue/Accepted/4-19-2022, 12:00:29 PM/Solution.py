// https://leetcode.com/problems/number-of-visible-people-in-a-queue

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        minions=[]
        n=len(heights)
        see=[0]*n
        
        
        for i in range(n-1,-1,-1):
            total=0
            while minions and heights[i]>minions[-1]:
                minions.pop()
                total+=1
                
            if minions:
                total+=1
                
            minions.append(heights[i])
            see[i]=total
            
        return see