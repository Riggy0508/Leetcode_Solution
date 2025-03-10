// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount=0
        maxC=0

        left=0
        right=0
        
        while right<len(nums)-1:
            if nums[right]==0:
                zeroCount+=1

            while zeroCount>k:
                if nums[left]==0:
                    zeroCount-=1
                left+=1

            maxC=max(maxC,right-left+1)
            right+=1

        return maxC
