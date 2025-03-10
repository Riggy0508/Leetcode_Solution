// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS,mapT={},{}
        
        
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            
            if (c1 in mapS and mapS[c1]!=c2) or (c2 in mapT and mapT[c2]!=c1):
                return False
            
            mapS[c1]=c2
            mapT[c2]=c1
        return True