// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC=count=0


        for num in nums:
            if num==1:
                count+=1
            else:
                maxC=max(maxC,count)
                count=0


        return max(maxC,count)
        