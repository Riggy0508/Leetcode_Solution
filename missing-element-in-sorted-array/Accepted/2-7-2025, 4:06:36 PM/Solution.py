// https://leetcode.com/problems/missing-element-in-sorted-array

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def missingCount(i):
            return nums[i]-nums[0]-i
        
        if missingCount(n-1)<k:
            return nums[n-1]+(k-missingCount(n-1))


        low,high=0,len(nums)-1

        while low<high:
            mid=(low+high)//2

            if missingCount(mid)<k:
                low=mid+1
            else:
                high=mid

        return nums[low-1]+(k-missingCount(low-1))

        