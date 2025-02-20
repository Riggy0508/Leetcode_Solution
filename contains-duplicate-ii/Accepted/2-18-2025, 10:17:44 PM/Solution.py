// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash1={}

        for i,val in enumerate(nums):
            if val in hash1 and i-hash1[val]<=k:
                return True
            hash1[val]=i
        return False