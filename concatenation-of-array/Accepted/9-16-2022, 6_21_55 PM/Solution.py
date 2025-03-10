// https://leetcode.com/problems/concatenation-of-array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0 for _ in range(2*n)]
        
        left=0
        right=n
        for i in range(n):
            ans[left]=nums[i]
            ans[right]=nums[i]
            left+=1
            right+=1
        return ans
        