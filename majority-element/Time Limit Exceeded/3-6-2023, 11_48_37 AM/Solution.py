// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=len(nums)//2

        for num in nums:
            count=sum(1 for elum in nums if elum==num)
            if count>majority:
                return num