// https://leetcode.com/problems/arithmetic-slices

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N=len(nums)
        dp=[None]*(N-1)
        
        for i in range(1,N):
            dp[i-1]=nums[i]-nums[i-1]
        
        output=0
        m=1
        for i in range(1,len(dp)):
            if dp[i-1]==dp[i]:
                output+=m
                m+=1
            else:
                m=1
        return output
            