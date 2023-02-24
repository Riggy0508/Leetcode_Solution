// https://leetcode.com/problems/arithmetic-slices

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        output=0
        m=1

        dp=[0]*(n-1)

        for i in range(1,n):
            dp[i-1]=nums[i]-nums[i-1]

        for i in range(1,len(dp)):
            if dp[i]==dp[i-1]:
                output+=m
                m+=1
            else:
                m=1
        return output

        

        return 1