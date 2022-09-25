// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        if (len(nums)==1):
            return [nums.copy()]    #need to return list of lits, Hint is given in the 3rd example. 
        
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
            