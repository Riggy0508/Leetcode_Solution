// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash1={}
        for word in s:
            if word in hash1:
                hash1[word]+=1
            else:
                hash1[word]=1
        
        for i in range(len(t)):
            if t[i] in hash1:
                 hash1[t[i]]-=1
            else:
                return False
        return True

