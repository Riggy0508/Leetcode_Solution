// https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0
        s=len(isConnected)
        seen=set()
        
        def dfs(p):
            for q, adj in enumerate(isConnected[p]):
                #print(q,adj)
                if (adj==1 and (q not in seen)):
                    seen.add(q)
                    dfs(q)

        count1=0
        for i in range(s):
            if i not in seen:
                dfs(i)
                count1+=1
        return count1
        