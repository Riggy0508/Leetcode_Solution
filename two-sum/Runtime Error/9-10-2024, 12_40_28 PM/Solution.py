// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1=[]
        diff=0
        for i,val in enum(nums):
            diff=target-nums[i]
            if diff in hash1:
                return [val,hash1[i]]
            hash1[i]=val