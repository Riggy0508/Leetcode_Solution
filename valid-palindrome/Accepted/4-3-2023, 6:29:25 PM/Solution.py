// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #write the code to lowercase all the letters and remove non-char elements
        s=''.join(ch for ch in s if ch.isalnum()).lower()
        
        l,r=0,len(s)-1

        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True