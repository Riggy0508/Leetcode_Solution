// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]

        for start,end in points:
            dist=start**2+end**2
            heapq.heappush(max_heap,(-dist,start,end))

            if len(max_heap)>k:
                heapq.heappop(max_heap)

        return [[start,end] for _,start,end in max_heap]