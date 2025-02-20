// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i=0
        n=len(nums)

        for j in range(1,n):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1