// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max1=0
        result=[]

        for i in range(len(heights)-1,-1,-1):
            if heights[i]>max1:
                max1=heights[i]
                result.append(i)

        return result[::-1]