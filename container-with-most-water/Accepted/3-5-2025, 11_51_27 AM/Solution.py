// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxA=0

        while left < right:
            area=(right-left)*min(height[right],height[left])
            maxA=max(maxA,area)


            if height[left]<height[right]:
                left+=1
            
            else:
                right-=1

        return maxA