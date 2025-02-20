// https://leetcode.com/problems/top-k-frequent-words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        hash1={}

        for word in words:
            if word in hash1:
                hash1[word]+=1
            else:
                hash1[word]=1


        heap=[]
        for word,freq in hash1.items():
            heapq.heappush(heap,(-freq,word))
            # if len(heap)>k:
            #     heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]