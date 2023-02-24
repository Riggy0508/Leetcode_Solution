// https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)

        pivot=0

        for i in range(n-1):
            if nums[i-1]<nums[i]:
                pivot=i
                break
        
        if pivot==0:
            return nums.sort()