// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        startTime=sorted(s[0] for s in intervals)
        endTime=sorted(s[1] for s in intervals)
       # print(startTime,endTime)
        s,e=0,0
        res=0
        ans=0
        
        while s<n:
            if startTime[s]<endTime[e]:
                s+=1
                ans+=1
            else:
                e+=1
                ans-=1
            res=max(res,ans)
        return res
        