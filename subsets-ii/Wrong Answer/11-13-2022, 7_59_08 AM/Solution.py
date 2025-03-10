// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output=[]
        
        def backtrack(first=0,curr=[]):
            if len(curr)==k:
                output.append(curr.copy())
                return
            
            for i in range(first,n):
                if i > first and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        
        n=len(nums)
        for k in range(n+1):
            backtrack()
        return output