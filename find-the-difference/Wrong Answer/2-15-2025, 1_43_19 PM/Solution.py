// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash1={}
        for ch in s:
            hash1[ch]=1


        for ch in t:
            if ch not in hash1 or hash1[ch]==0:
                return ch
            
            else:
                hash1[ch]-=1