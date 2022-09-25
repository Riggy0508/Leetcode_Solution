// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n=len(heights)
        result=[]
        
        for curBuild in range(n):
            while result and heights[result[-1]]<=heights[curBuild]:
                result.pop()
            result.append(curBuild)
        return result