// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]
        visited=set()

        def backtrack(subset=[]):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(subset+[nums[i]])
                    visited.remove(i)

        backtrack()
        return res