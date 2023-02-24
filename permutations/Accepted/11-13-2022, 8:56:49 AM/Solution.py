// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        n=len(nums)
        visited=set()
        
        def backtrack(subset=[]):
            if len(subset)==len(nums):
                output.append(subset.copy())
                return
            
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    backtrack(subset+[nums[i]])
                    visited.remove(i)
            
        backtrack()
        return output