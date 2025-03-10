// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap=[]

        hash1={}

        for num in nums:
            if num in hash1:
                hash1[num]+=1

            else:
                hash1[num]=1


        for num,freq in hash1.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [num for freq,num in min_heap]