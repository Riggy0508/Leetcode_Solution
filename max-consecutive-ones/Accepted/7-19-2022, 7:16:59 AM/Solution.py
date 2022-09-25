// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=max_count=0
        
        for n in nums:
            if n==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
            
        return max(max_count,count)