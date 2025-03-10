// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        curSum=0

        for num in nums:
            curSum+=num
            if curSum<0:
                curSum=0
            maxSub=max(maxSub,curSum)

        return maxSub
            


