// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        
        
        def backtrack(remain,list1,start):
            if remain==0:
                results.append(list1.copy())
                
            elif remain<0:
                return
            
            
            for i in range(start,len(candidates)):
                list1.append(candidates[i])
                
                backtrack(remain-candidates[i],list1,i)
                
                list1.pop()
        
        
        
        
        
        backtrack(target,[],0)
        return results