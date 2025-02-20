// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash1={}

        for num in nums:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1


        min_heap=[]
        for i,val in hash1.items():
            heapq.heappush(min_heap,(i,val))

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [i for _,i in min_heap]