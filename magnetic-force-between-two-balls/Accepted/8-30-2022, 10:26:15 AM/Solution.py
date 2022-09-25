// https://leetcode.com/problems/magnetic-force-between-two-balls

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l=1
        r=max(position)
        ans=0
        
        while l<=r:
            mid=l+(r-l)//2
            count=1
            prev=position[0]
            for p in position:
                if p-prev>=mid:
                    count+=1
                    prev=p
                    if count>m:
                        break
            if count>=m:
                ans=max(ans,mid)
                l=mid+1
            else:
                r=mid-1
                
        return ans