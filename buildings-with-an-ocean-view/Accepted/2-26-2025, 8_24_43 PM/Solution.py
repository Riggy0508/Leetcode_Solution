// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxC=0
        result=[]


        for i in range(len(heights)-1,-1,-1):
            if heights[i]>maxC:
                maxC=heights[i]
                result.append(i)

        return sorted(result)