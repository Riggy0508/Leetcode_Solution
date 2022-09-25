// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            complement=target-nums[i];
            if complement in hashMap:
                return [i,hashMap[complement]]
            hashMap[nums[i]]=i
        
        