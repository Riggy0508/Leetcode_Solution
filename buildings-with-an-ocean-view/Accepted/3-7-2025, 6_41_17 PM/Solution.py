// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result=[]
        maxH=0
        
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>maxH:
                result.append(i)
                maxH=heights[i]

        return sorted(result)