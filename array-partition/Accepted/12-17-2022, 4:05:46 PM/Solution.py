// https://leetcode.com/problems/array-partition

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum_max=0

        nums.sort()
        print(nums)
        for i in range(0,len(nums),2):
            print(nums[i])
            sum_max+=nums[i]
        return sum_max
