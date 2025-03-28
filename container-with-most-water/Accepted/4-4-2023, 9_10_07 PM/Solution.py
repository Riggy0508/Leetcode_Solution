// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0

        l=0
        r=len(height)-1
        res=0

        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res