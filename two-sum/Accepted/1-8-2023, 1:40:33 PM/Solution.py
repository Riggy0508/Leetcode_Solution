// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the index of numbers who's sum add's up to target

        hash1={}

        for i,val in enumerate(nums):
            diff=target-val
            if val in hash1:
                return [hash1[val],i]
            hash1[diff]=i