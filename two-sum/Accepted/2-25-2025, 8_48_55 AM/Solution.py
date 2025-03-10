// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}


        for i,val in enumerate(nums):
            diff=target-val
            if diff in hash1:
                return [i,hash1[diff]]
            hash1[val]=i