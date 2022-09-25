// https://leetcode.com/problems/find-the-middle-index-in-array

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        n=0
        
        for i in range(len(nums)):
            if n==total-n-nums[i]:
                return i
            n+=nums[i]
            
        return -1
            