// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash1={}

        for i in range(len(nums)):
            if nums[i] in hash1:
                return True
            else:
                hash1[nums[i]]=1
        return False