// https://leetcode.com/problems/concatenation-of-array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums