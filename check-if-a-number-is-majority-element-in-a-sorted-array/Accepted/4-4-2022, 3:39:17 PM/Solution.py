// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if (nums.count(target)>len(nums)//2):
            return True