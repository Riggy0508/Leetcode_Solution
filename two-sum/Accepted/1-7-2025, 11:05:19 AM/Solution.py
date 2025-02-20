// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff=0
        hash1={}

        for i,val in enumerate(nums):
            diff=target-nums[i]

            if diff in hash1:
                return [hash1[diff],i]
            hash1[val]=i

        return -1