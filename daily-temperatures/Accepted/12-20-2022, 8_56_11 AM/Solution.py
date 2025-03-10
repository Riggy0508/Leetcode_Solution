// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)

        stack=[] #In this stack we are gonna keep a pair of [temp,index]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                temp,index=stack.pop()
                res[index]=(i-index)
            stack.append([t,i])
        return res