// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalin(l,r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                count+=1
            return count

        count=0
        for i in range(len(s)):
            count+=isPalin(i,i)  #odd string
            count+=isPalin(i,i+1)#even strings

        return count
            