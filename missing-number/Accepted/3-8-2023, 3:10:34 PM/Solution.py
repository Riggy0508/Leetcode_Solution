// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=sum(nums)
        sum2=n*(n+1)//2
        return sum2-sum1