// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash1={}

        for n in nums:
            if n in hash1:
                return True
            hash1[n]=1
        return False