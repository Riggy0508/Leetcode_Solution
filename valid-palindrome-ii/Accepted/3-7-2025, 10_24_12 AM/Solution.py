// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return (self.isPali(s,l+1,r) or self.isPali(s,l,r-1))
            else:
                l+=1
                r-=1

        return True


    def isPali(self,s,l,r):
        while l<=r:
            if s[l]!=s[r]:
                return False

            l+=1
            r-=1

        return True
            