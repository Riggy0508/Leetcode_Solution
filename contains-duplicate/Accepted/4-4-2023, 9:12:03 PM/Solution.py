// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash1={}

        for i in nums:
            if i in hash1:
                return True
            else:
                hash1[i]=i
        return False