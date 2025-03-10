// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxL=0
        left=0
        zero=0

        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1

            maxL=max(maxL,right-left+1)

        return maxL
                