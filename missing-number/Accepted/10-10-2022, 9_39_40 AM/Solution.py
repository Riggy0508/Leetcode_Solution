// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ex=n*(n+1)//2
        ac=sum(nums)
        return ex-ac