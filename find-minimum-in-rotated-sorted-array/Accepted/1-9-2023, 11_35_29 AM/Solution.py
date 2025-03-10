// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[0]


        while l<=r:


            if nums[l]<nums[r]:
                res=min(nums[l],res)
                return res

            m=(l+r)//2
            res=min(nums[m],res)
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res
