// https://leetcode.com/problems/reorganize-string

class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        maxHeap=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(maxHeap) #O(n) 
        
        prev=None
        res=""
        
        while maxHeap or prev:
            #we want the most frequent excluding the prev number
            
            if prev and not maxHeap:
                return ""
            cnt,char=heapq.heappop(maxHeap)
            #print(cnt,char)
            res+=char
            cnt+=1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev=None
            if cnt !=0:
                prev=[cnt,char]
        return res
            