// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1=Counter(s)
        #print(c1)
        for ch in t:
            #print(ch)
            if ch not in c1 or c1[ch]==0:
                return ch
            else:
                c1[ch]-=1