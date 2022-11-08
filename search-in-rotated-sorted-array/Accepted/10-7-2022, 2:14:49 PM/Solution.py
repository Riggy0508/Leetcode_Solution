// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            
            #Now we are gonna search in the left sorted portion
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            #Now checking in the right sorted portion
            else:
                if target< nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
                
            