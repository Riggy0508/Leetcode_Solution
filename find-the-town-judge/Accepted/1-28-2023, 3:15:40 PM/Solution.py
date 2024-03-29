// https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        out=[0]*(n+1)
        into=[0]*(n+1)
        for a,b in trust:
            out[a]+=1
            into[b]+=1



        for i in range(1,n+1):
            if out[i]==0 and into[i]==n-1:
                return i

        return -1
            