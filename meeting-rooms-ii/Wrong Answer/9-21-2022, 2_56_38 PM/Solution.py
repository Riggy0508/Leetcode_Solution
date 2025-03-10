// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTime=sorted(s[0] for s in intervals)
        endTime=sorted(s[1] for s in intervals)
        
        s,e=0,0
        cm,res=0,0
        
        while s<len(intervals):
            if startTime[s]<=endTime[e]:
                s+=1
                cm+=1
            else:
                e+=1
                cm-=1
            res=max(res,cm)
        return res
        