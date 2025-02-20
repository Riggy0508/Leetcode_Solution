// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen=set()

        for i,val in enumerate(nums):
            if val not in seen:
                seen.add(val)

            else:
                return True
            if i>=k:
                seen.remove(nums[i-k])

        return False
