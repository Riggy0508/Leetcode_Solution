// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left=self.searchBinary(nums,target,isLeft=True)
        right=self.searchBinary(nums, target,isLeft=False)

        return [left,right]


    def searchBinary(self,nums,target,isLeft):
        l=0
        r=len(nums)-1
        i=-1

        while l<=r:
            mid=(l+r)//2

            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                i=mid
                if isLeft:
                    r=mid-1
                else:
                    l=mid+1

        return i