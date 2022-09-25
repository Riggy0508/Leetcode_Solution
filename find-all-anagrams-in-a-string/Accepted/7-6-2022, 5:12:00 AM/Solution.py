// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        
        pCounter,sCounter={},{}
        
        for i in range(len(p)):
            pCounter[p[i]]=1+pCounter.get(p[i],0)
            sCounter[s[i]]=1+sCounter.get(s[i],0)
            
        res=[0] if pCounter==sCounter else []
        
        l=0
        for r in range(len(p),len(s)):
            sCounter[s[r]]=1+sCounter.get(s[r],0)
            sCounter[s[l]]-=1
            
            
            if sCounter[s[l]]==0:
                sCounter.pop(s[l])
            
            l+=1
            if sCounter==pCounter:
                res.append(l)
        return res