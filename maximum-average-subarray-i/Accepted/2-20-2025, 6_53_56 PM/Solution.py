// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum=sum(nums[:k])
        maxSum=window_sum


        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            maxSum=max(maxSum,window_sum)

        return maxSum/k