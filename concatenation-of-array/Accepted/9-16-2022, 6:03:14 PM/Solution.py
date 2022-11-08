// https://leetcode.com/problems/concatenation-of-array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [0] * (2 * n)
        
        left = 0
        right = n
        
        for idx in range(n):
            ans[left] = nums[idx]
            ans[right] = nums[idx]
            left += 1
            right += 1
        
        return ans