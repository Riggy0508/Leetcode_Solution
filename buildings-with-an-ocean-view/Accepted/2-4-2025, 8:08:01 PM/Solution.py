// https://leetcode.com/problems/buildings-with-an-ocean-view

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        max_height=0
        result=[]

        for i in range(len(heights)-1,-1,-1):
            if heights[i]>max_height:
                result.append(i)
                max_height=heights[i]
        

        return result[::-1]