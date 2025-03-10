// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax,curMin=1,1

        for n in nums:
            if n==0:
                curMax,curMin=1,1
                continue
            temp=n*curMax
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(temp,n*curMin,n)
            res=max(res,curMax)
        return res
