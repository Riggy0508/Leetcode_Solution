// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch for ch in s if ch.isalnum()).lower()
        l=0
        r=len(s)-1
        if len(s)==0:
            return True
        while l<r:
            #print(s[l],s[r])
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
            
        return True
        