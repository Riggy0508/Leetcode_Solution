// https://leetcode.com/problems/missing-element-in-sorted-array

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n=len(nums)

        def missingCount(i):
            return (nums[i]-nums[0])-i

        if missingCount(n-1)<k:
            return nums[-1]+(k-missingCount(n-1))

        
        l,r=0,n-1

        while l<r:
            mid=(l+r)//2

            if missingCount(mid)<k:
                l=mid+1
            else:
                r=mid

        return nums[l-1]+(k-missingCount(l-1))