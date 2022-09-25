// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        
        for num,val in enumerate(nums):
            if val in hash and num-hash[val]<=k:
                return True
            else:
                hash[val]=num
        return False