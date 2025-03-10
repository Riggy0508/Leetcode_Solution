// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        curSum=0

        for num in nums:
            curSum+=num
            maxSub=max(maxSub,curSum)
            if curSum<0:
                curSum=0
            

        return maxSub
            


