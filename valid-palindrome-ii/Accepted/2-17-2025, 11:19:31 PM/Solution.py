// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                if self.ifPalindrome(s,l+1,r) or self.ifPalindrome(s,l,r-1):
                    return True
                else:
                    return False
            l+=1
            r-=1

        return True

        



    def ifPalindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1

        return True