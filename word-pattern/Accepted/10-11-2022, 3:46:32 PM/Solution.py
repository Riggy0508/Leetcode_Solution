// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s=s.split(" ")
        mapP={}
        mapS={}
        
        if len(pattern)!=len(s):
            return False
        
        for i in range(len(s)):
            c1=pattern[i]
            c2=s[i]
            
            if (c1 in mapP and mapP[c1]!=c2) or (c2 in mapS and mapS[c2]!=c1):
                return False
            
            mapP[c1]=c2
            mapS[c2]=c1
            
        return True
            
        
        