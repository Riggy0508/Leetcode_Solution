// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        
        def dfs(used_number,nums):
            if len(used_number)==n:
                result.append(used_number.copy())
                return 
            
            for i,num in enumerate(nums):
                used_number.append(num)
                dfs(used_number,nums[:i]+nums[i+1:])
                used_number.pop()
                    
        dfs([],nums)
        return result