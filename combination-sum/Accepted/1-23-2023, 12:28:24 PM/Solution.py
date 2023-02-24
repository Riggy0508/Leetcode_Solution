// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]


        def backtrack(remain,curr,start):
            if remain==0:
                output.append(curr.copy())
                return
            
            if remain<0:
                return

            for j in range(start,len(candidates)):
                curr.append(candidates[j])
                backtrack(remain-candidates[j],curr,j)
                curr.pop()

        backtrack(target,[],0)
        return output