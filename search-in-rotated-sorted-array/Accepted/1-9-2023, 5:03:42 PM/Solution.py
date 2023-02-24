// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1


        while l<=r:
            m=(l+r)//2

            if nums[m]==target:
                return m

            if nums[m]>=nums[l]:
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1

            else:
                if target>nums[r] or target <nums[m]:
                    r=m-1
                else:
                    l=m+1
        return -1
