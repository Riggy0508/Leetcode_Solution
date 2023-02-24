// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        prefixSum=[sum(nums[:i+1]) for i in range(len(nums))]

        minVal=min(prefixSum)

        if minVal<=0:
            return abs(minVal)+1
        else:
            return 1  


        