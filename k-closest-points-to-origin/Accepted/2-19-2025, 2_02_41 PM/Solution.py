// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]


        for x,y in points:
            dist=-(x**2+y**2)
            heapq.heappush(max_heap,(dist,x,y))

            if len(max_heap)>k:
                heapq.heappop(max_heap)

        return [[x,y] for _,x,y in max_heap]