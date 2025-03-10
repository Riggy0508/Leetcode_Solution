// https://leetcode.com/problems/valid-palindrome-iii

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        #@lru_cache(None)
        def dp(l,r,k):
            if k<0:
                return False
            if l>=r:
                return True
            if s[l]==s[r]:
                return dp(l+1, r-1, k)
            else:
                return dp(l+1, r, k-1) or dp(l,r-1,k-1)

        return dp(0,len(s)-1,k) 