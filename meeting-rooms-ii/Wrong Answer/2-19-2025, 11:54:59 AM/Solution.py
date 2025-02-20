// https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_heap=[]

        intervals.sort()

        for start,end in intervals:
            if min_heap and min_heap[0]<start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,end)

        return len(min_heap)