// https://leetcode.com/problems/minimum-distance-to-the-target-element

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min1=float("inf")

        for i in range(len(nums)):
            if nums[i]==target:
                if min1>abs(i-start):
                    min1=abs(i-start)
        
        return min1
    