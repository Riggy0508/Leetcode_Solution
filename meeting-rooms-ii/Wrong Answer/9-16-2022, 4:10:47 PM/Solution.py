// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTime=sorted([s[0] for s in intervals])
        endTime=sorted([s[1] for s in intervals])
        
        si,ei=0,0
        nList=0
        mList=0
        while si<len(startTime):
            if startTime[si]<endTime[ei]:
                si+=1
                nList+=1
            else:
                ei+=1
                mList=mList+max(nList,mList)
                
        return mList
                