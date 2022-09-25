// https://leetcode.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[] # this is a mono stack with a pair which stores number and the minimum count
        curMin=nums[0]
        
        for n in (nums[1:]):
            while stack and n>=stack[-1][0]:
                stack.pop()
            if stack and n>stack[-1][1]:
                return True
            stack.append([n,curMin])
            curMin = min(n,curMin)
            
        return False