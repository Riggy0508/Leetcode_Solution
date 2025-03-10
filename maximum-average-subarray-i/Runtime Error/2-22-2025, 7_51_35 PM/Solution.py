// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum

        for i in range(k,len(nums)):
            window_sum=sum(nums[:k]-nums[i-1:k])
            max_sum=max(max_sum,window_sum)


        return max_sum/k