// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if (nums[r]!=nums[r-1]):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l      