// https://leetcode.com/problems/concatenation-of-array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        r=[]
        
        for i in range(0,2*n):
            if i<n:
                r.append(nums[i])
            else:
                r.append(nums[i-n])
                
        return r