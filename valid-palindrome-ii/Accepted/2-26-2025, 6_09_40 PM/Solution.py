// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                skipl=s[l+1:r+1]
                skipr=s[l:r]
                return skipl==skipl[::-1] or skipr==skipr[::-1]
            else:
                l+=1
                r-=1

        return True