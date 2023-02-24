// https://leetcode.com/problems/next-greater-element-ii

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)

        for i in range(2):
            for i,val in enumerate(nums):
                while stack and val>nums[stack[-1]]:
                    res[stack.pop()]=val
                stack.append(i)
            
        return res