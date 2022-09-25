// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hash1:
                return [i,hash1[diff]]
            hash1[nums[i]]=i