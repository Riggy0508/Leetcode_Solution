// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N=len(s)
        Dict=set(wordDict)
        dp1=[False for _ in range(N+1)]
        dp1[0]=True
        
        for start in range(N):
            for end in range(start+1,N+1):
                if dp1[start] and s[start:end] in Dict:
                        dp1[end]=True
        
        if not dp1[-1]: return []
        
        dp=[[] for _ in range(N+1)]
        dp[0]=[""]
        
        for start in range(N):
            for end in range(start+1,N+1):
                if s[start:end] in Dict:
                    for sub in dp[start]:
                        dp[end].append(sub+" "+s[start:end])
                        
        return [s[1:] for s in dp[-1]]