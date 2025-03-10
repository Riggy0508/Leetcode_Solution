// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxL=0
        left=0
        zeroCnt=0

        for r in range(len(nums)):
            if nums[r]==0:
                zeroCnt+=1

            while zeroCnt>k:
                if nums[left]==0:
                    zeroCnt-=1

                left+=1


            maxL=max(maxL,r-left+1)

        return maxL