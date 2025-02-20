// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1={}

        for num in nums:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1

        heap=[]
        for num,freq in hash1.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)

        return [num for freq,num in heap]

