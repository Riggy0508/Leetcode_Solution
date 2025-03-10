// https://leetcode.com/problems/continuous-subarrays

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        l,result=0,0
        min1,max1=nums[0],nums[0]

        for r in range(len(nums)):
            max1=max(max1,nums[r])
            min1=min(min1,nums[r])

            while max1-min1>2:
                l+=1
                if nums[l-1]==min1 or nums[l-1]==max1:
                    max1=max(nums[l:r+1])
                    min1=min(nums[l:r+1])

            result+=(r-l+1)

        return result
