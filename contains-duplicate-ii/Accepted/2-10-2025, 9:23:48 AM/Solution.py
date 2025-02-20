// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()

        for i,val in enumerate(nums):
            if val in seen:
                return True

            seen.add(val)
            
            if i>=k:
                seen.remove(nums[i-k])

        return False