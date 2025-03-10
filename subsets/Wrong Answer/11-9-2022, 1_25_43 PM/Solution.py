// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=1,curr=[]):
            if len(curr)==k:
                output.append(curr.copy())
                return
            
            for i in range(first,n+1):
                curr.append(i)
                
                backtrack(i+1,curr)
                
                curr.pop()
        
        
        output=[]
        n=len(nums)
        
        for k in range(n+1):
            backtrack()
        return output