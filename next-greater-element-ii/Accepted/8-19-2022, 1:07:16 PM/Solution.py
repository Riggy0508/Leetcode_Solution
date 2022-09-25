// https://leetcode.com/problems/next-greater-element-ii

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1 for _ in nums]
        
        for _ in range(2):
            for i,num in enumerate(nums):
                while stack and num>nums[stack[-1]]:
                    result[stack.pop()]=num
                stack.append(i)
                
        return result