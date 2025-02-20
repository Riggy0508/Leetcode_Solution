// https://leetcode.com/problems/missing-ranges

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing_range=[]
        n=len(nums)

        if n==0:
            return missing_range.append([lower,upper])

        if lower<nums[0]:
            missing_range.append([lower,nums[0]-1])

        for i in range(n-1):
            if nums[i+1]-nums[i]<=1:
                continue
            missing_range.append([nums[i]+1,nums[i+1]-1])

        if upper>nums[n-1]:
            missing_range.append([nums[n-1]+1,upper])

        return missing_range

