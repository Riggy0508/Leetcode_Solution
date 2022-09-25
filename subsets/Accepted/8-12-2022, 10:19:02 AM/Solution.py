// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        subset=[]
        
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            #including the nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            #excluding the nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res