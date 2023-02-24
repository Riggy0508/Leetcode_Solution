// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted(s[0] for s in intervals)
        end=sorted(e[1] for e in intervals)
        
        res,count=0,0
        s,e=0,0
        while s<len(intervals):
            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res=max(res,count)
        return res
        

        
        