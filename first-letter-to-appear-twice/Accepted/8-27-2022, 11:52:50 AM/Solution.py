// https://leetcode.com/problems/first-letter-to-appear-twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash1={}
        
        for i in range(len(s)):                   
            if s[i] not in hash1:
                hash1[s[i]]=1
            else:
                return s[i]