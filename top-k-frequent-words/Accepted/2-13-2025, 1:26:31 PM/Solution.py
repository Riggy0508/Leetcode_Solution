// https://leetcode.com/problems/top-k-frequent-words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash1={}

        for word in words:
            if word in hash1:
                hash1[word]+=1
            else:
                hash1[word]=1



        max_heap=[]

        for word,count in hash1.items():
            heapq.heappush(max_heap,(-count,word))


        return [heapq.heappop(max_heap)[1] for _ in range(k)]

        