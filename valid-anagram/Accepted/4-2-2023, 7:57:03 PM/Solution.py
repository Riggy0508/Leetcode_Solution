// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hash1={}
        hash2={}

        for word in s:
            if word in hash1:
                hash1[word]+=1
            else:
                hash1[word]=1
        for word in t:
            if word in hash1:
                hash1[word]-=1
            else:
                return False
        
        for h in hash1:
            if hash1[h]!=0:
                return False
        return True
        

            