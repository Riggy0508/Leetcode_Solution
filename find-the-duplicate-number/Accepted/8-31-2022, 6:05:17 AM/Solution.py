// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash1={}
        for i in range(len(nums)):
            if nums[i] not in hash1:
                hash1[nums[i]]=nums[i]
            else:
                return nums[i]
                
            