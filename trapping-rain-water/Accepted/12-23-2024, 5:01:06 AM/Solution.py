// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l,r=0,len(height)-1
        maxL,maxR=height[l],height[r]
        res=0

        while l<r:
            if height[l]<height[r]:
                l+=1
                maxL=max(height[l],maxL)
                res+=maxL-height[l]

            else:
                r-=1
                maxR=max(height[r],maxR)
                res+=maxR-height[r]

        return res