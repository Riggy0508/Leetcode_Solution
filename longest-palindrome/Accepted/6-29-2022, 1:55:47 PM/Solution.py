// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        output=0
        
        for count in c.values():
            #print("C:",count)
            output+=int(count/2)*2
            if output%2==0 and count%2==1:
                output+=1
        return output