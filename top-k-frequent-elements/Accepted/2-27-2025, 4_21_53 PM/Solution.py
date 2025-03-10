// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash1={}
        min_heap=[]

        for num in nums:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1


        for i,freq in hash1.items():
            heapq.heappush(min_heap,(freq,i))

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [i for _,i in min_heap]