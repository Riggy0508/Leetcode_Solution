// https://leetcode.com/problems/continuous-subarrays

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        l,result=0,0

        for r in range(len(nums)):
            current_window=nums[l:r+1]
            min1,max1=min(current_window),max(current_window)

            while max1-min1>2:
                l+=1
                current_window=nums[l:r+1]
                min1,max1=min(current_window),max(current_window)

            result+=(r-l+1)

        return result
