// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        
        for index,temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                stackIndex=stack.pop()
                res[stackIndex]=(index-stackIndex)
            stack.append(index)
        return res
            