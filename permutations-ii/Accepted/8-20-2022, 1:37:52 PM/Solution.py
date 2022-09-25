// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        hash1={n:0 for n in nums}
        
        for n in nums:
            hash1[n]+=1
        
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            
            for h in hash1:
                if hash1[h]>0:
                    perm.append(h)
                    hash1[h]-=1
                    
                    dfs()
                    
                    hash1[h]+=1
                    perm.pop()
                    
                
        
        
        
        dfs()
        return res