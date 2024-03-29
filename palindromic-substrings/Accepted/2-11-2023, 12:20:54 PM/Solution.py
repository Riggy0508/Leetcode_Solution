// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        #the length of the string can be even and odd
        res=0
        for i in range(len(s)):
            res+=self.pali(s,i,i)
            res+=self.pali(s,i,i+1)
        return res

    def pali(self,s,l,r):
        res=0

        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res


        