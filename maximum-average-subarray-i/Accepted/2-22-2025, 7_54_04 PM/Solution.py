// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        max1=window

        for i in range(k,len(nums)):
            window+=nums[i]-nums[i-k]
            max1=max(max1,window)

        return max1/k