// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        positive=0
        negative=0

        for n in nums:
            if n<0:
                negative+=1
            elif n>1:
                positive+=1
        
        return max(positive,negative)
            
        