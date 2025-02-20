// https://leetcode.com/problems/meeting-rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if len(intervals)==0:
            return True
        prevEnd=0
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
            else:
                return True