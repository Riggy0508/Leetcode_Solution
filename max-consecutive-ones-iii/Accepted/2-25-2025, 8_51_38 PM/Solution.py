// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lc=zc=0
        left=right=0

        while right<len(nums):
            if nums[right]==0:
                zc+=1

            while zc>k:
                if nums[left]==0:
                    zc-=1
                left+=1

            lc=max(lc,right-left+1)
            right+=1

        return lc