// https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        pivot=0

        for i in range(n,0,-1):
            if nums[i-1]<nums[i]:
                pivot=i
                break


        if pivot==0:
            return nums.sort()

        swap=n
        while nums[pivot-1]>nums[swap]:
            swap-=1


        nums[pivot-1],nums[swap]=nums[swap],nums[pivot-1]
        nums[pivot:]=reversed(nums[pivot:])
