// https://leetcode.com/problems/max-consecutive-ones-ii

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls=zc=0


        left,right=0,0

        while right<len(nums):
            if nums[right]==0:
                zc+=1
            
            while zc>=2:
                if nums[left]==0:
                    zc-=1
                left+=1

            ls=max(ls,right-left+1)
            right+=1

        return ls
